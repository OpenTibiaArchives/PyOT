spidris = genMonster("Spidris", (457, 15296), "a spidris")
spidris.health(3700, healthmax=3700)
spidris.type("slime")
spidris.defense(armor=50, fire=0.95, earth=0, energy=1.05, ice=1.05, holy=1.1, death=0.95, physical=1, drown=1)
spidris.experience(2600)
spidris.speed(350) #incorrect
spidris.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
spidris.walkAround(energy=1, fire=1, poison=0)
spidris.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
spidris.voices("Eeeeeeyyyyh!")
spidris.regMelee(300)