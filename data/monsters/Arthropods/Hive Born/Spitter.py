spitter = genMonster("Spitter", (461, 15392), "a spitter")
spitter.health(1500)
spitter.type("slime")
spitter.defense(armor=1, fire=0.95, earth=0, energy=1.05, ice=1.05, holy=1, death=0.95, physical=1, drown=1)
spitter.experience(1100)
spitter.speed(300) #incorrect
spitter.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=40)
spitter.walkAround(energy=1, fire=1, poison=0)
spitter.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
spitter.regMelee(150)