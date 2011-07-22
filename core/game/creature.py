from game.engine import getSpectators
from packet import TibiaPacket
from game.map import placeCreature, removeCreature, getTile
import threading
import game.enum as enum

# Unique ids, thread safe too
def __uid():
    idsTaken = 1000
    while True:
        idsTaken += 1
        yield idsTaken
        
__uniqueId = __uid().next
__uniqueLock = threading.Lock()
def uniqueId():
    __uniqueLock.acquire()
    id = __uniqueId()
    __uniqueLock.release()
    return id

allCreatures = {}

class Creature:
    
    def __init__(self, data, position, cid=None):
        self.data = data
        self.creatureType = 0
        self.direction = 0
        self.position = position
        self.speed = 0x0032
        self.scripts = {"onWalk":None, "onNextStep":[]}
        self.cid = cid if cid else self.generateClientID()
        self.outfit = [self.data["looktype"], self.data["lookhead"], self.data["lookbody"], self.data["looklegs"], self.data["lookfeet"]]
        self.mount = 0
        self.mounted = 0
        self.addon = 0
        self.action = None
        self.actionLock = threading.Lock()
        
        # We are trackable
        allCreatures[self.cid] = self
        
    def name(self):
        return self.data["name"]

    def clientId(self):
        return self.cid

    def generateClientID(self):
        raise NotImplementedError("This function must be overrided by a secondary level class!")
        
    def stepDuration(self, tile):
        return (tile.speed / self.speed) # TODO

    def move(self, direction, spectators=None):
        import data.map.info
        
        self.direction = direction
        
        # Make packet
        stream = TibiaPacket(0x6D)
        stream.position(self.position)
        stream.uint8(getTile(self.position).findCreatureStackpos(self))
        
        
        # Recalculate position
        position = self.position[:] # Important not to remove the : here, we don't want a reference!
        if direction is 0:
            position[1] = self.position[1] - 1
        elif direction is 1:
            position[0] = self.position[0] + 1
        elif direction is 2:
            position[1] = self.position[1] + 1
        elif direction is 3:
            position[0] = self.position[0] - 1
        elif direction is 4:
            position[1] = self.position[1] + 1
            position[0] = self.position[0] - 1
        elif direction is 5:
            position[1] = self.position[1] + 1
            position[0] = self.position[0] + 1
        elif direction is 6:
            position[1] = self.position[1] - 1
            position[0] = self.position[0] - 1
        elif direction is 7:
            position[1] = self.position[1] - 1
            position[0] = self.position[0] + 1
            
        # We don't walk out of the map!
        if position[0] < 1 or position[1] < 1 or position[0] > data.map.info.width or position[1] > data.map.info.height:
           return False
                    
        stream.position(position)
        print position
        newTile = getTile(position)
        
        if newTile.creatures(): # Dont walk to creatures
            return False
            
        removeCreature(self, self.position)
        placeCreature(self, position)
        
        self.position = position
        
        if self.scripts["onWalk"]:
            self.scripts["onWalk"]()
            del self.scripts["onWalk"]
        # Send to everyone   
        if not spectators:
            spectators = getSpectators(position)
        for spectator in spectators:
            if not self.cid in spectator.player.knownCreatures:
                stream2 = TibiaPacket()
                print "My pos (and creature %d): " % self.cid, spectator.player.position
                stream2.addTileCreature(position, 1, self, spectator.player)
                stream2.send(spectator)
                spectators.remove(spectator)
        
        stream.sendto(spectators) 
        
        return True # Required for auto walkings

    def say(self, message):
        stream = TibiaPacket(0xAA)
        stream.uint32(00)
        stream.string(self.data["name"])
        stream.uint16(self.data["level"] if "level" in self.data else 0)
        stream.uint8(enum.MSG_SPEAK_SAY)
        stream.position(self.position)
        stream.string(message)
        stream.sendto(getSpectators(self.position))

    def yell(self, message):
        stream = TibiaPacket(0xAA)
        stream.uint32(00)
        stream.string(self.data["name"])
        stream.uint16(self.data["level"] if "level" in self.data else 0)
        stream.uint8(enum.MSG_SPEAK_YELL)
        stream.position(self.position)
        stream.string(message)
        stream.sendto(getSpectators(self.position))
        
    def stopAction(self):
        try:
            self.action.cancel()
        except:
            pass
        del self.action
        
    def canSee(self, position):
        if abs(position[0]-self.position[0]) < 9 and abs(position[1]-self.position[1]) < 7:
            return True
        