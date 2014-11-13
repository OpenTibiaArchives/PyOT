
minotaur_mage = genMonster("Minotaur Mage", (23, 5981), "a minotaur mage")
minotaur_mage.health(155)
minotaur_mage.type("blood")
minotaur_mage.defense(armor=20, fire=1.1, earth=0.8, energy=0.8, ice=1, holy=0.9, death=1.05, physical=1, drown=1)
minotaur_mage.experience(150)
minotaur_mage.speed(170)
minotaur_mage.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=4, runOnHealth=0)
minotaur_mage.walkAround(energy=1, fire=1, poison=1)
minotaur_mage.immunity(paralyze=1, invisible=0, lifedrain=0, drunk=1)
minotaur_mage.voices("Learrn tha secrret uf deathhh!", "Kaplar!")
minotaur_mage.regMelee(20)
minotaur_mage.loot( ("minotaur horn", 4.25, 2), (2148, 100, 35), ("carrot", 58.0, 8), ("purple robe", 5.5), ("minotaur leather", 2.0, 3), ("leather legs", 5.0), ("torch", 4.5), ("leather helmet", 3.75), ("taurus mace", 0.75), ("wand of cosmic energy", 0.5), ("mana potion", 0.5) )