orc_spearman = genMonster("Orc Spearman", (50, 5996), "an orc spearman")
orc_spearman.health(105)
orc_spearman.type("blood")
orc_spearman.defense(armor=7, fire=1, earth=1.1, energy=0.8, ice=1, holy=0.8, death=1.1, physical=1, drown=1)
orc_spearman.experience(38)
orc_spearman.speed(176)
orc_spearman.behavior(summonable=310, hostile=True, illusionable=True, convinceable=310, pushable=True, pushItems=False, pushCreatures=False, targetDistance=4, runOnHealth=10)
orc_spearman.walkAround(energy=1, fire=1, poison=1)
orc_spearman.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
orc_spearman.voices("Ugaar!")
orc_spearman.regMelee(25)
orc_spearman.regDistance(30, ANIMATION_SPEAR, chance(21))
orc_spearman.loot( ("spear", 17.5), (2148, 100, 11), ("studded legs", 9.75), ("meat", 29.25), ("studded helmet", 9.25), ("machete", 2.75), ("orc leather", 2.0), ("orc tooth", 0.25) )