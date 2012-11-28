Versperoth = genMonster("Versperoth", (8, 5980), "a Versperoth") #rotworm queen look id, mostly unkown
Versperoth.setHealth(125000)
Versperoth.bloodType("blood")
Versperoth.setDefense(armor=65, fire=0.5, earth=1.05, energy=0.55, ice=0.55, holy=0.6, death=0.45, physical=0.7, drown=0.7)
Versperoth.setExperience(20000)
Versperoth.setSpeed(0)
Versperoth.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
Versperoth.walkAround(energy=0, fire=0, poison=0)
Versperoth.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Versperoth.voices("GrrroaR!", "GROWL!", "Waaaah!")
Versperoth.regMelee(900)