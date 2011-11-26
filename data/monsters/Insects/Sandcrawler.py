sandcrawler = game.monster.genMonster("sandcrawler", (350, 11360), "a sandcrawler")
sandcrawler.setHealth(30)
sandcrawler.bloodType(color="slime")
sandcrawler.setDefense(armor=5, fire=1.1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
sandcrawler.setExperience(20)
sandcrawler.setSpeed(230)
sandcrawler.setBehavior(summonable=250, hostile=1, illusionable=1, convinceable=250, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
sandcrawler.walkAround(energy=1, fire=1, poison=1)
sandcrawler.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
sandcrawler.voices("Chrk chrk!")
sandcrawler.regMelee(3)
sandcrawler.loot( (2148, 100, 6), ("sandcrawler shell", 1.75) )