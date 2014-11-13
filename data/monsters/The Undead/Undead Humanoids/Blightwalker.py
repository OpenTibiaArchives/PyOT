blightwalker = genMonster("Blightwalker", (246, 6354), "a blightwalker")
blightwalker.health(8900)
blightwalker.type("undead")
blightwalker.defense(armor=68, fire=0.5, earth=0, energy=0.8, ice=0.5, holy=1.3, death=0, physical=1.1, drown=1)
blightwalker.experience(5850)
blightwalker.speed(240)
blightwalker.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
blightwalker.walkAround(energy=1, fire=0, poison=0)
blightwalker.immunity(paralyze=1, invisible=1, lifedrain=0, drunk=0)
blightwalker.voices("I can see you decaying!", "Let me taste your mortality!", "Your lifeforce is waning!")
blightwalker.regMelee(490)
blightwalker.loot( ("bunch of wheat", 59.75), (2148, 100, 271), ("soul orb", 25.5), ("bundle of cursed straw", 10.0), ("rusty armor", 7.75), ("demonic essence", 30.25), ("poison arrow", 46.25, 12), ("blank rune", 38.5, 2), ("terra mantle", 0.5), ("great health potion", 9.5), ("scythe", 3.25), ("hailstorm rod", 7.75), ("seeds", 2.0), ("terra legs", 1.5), ("garlic necklace", 1.0), ("skull staff", 0.75), ("gold ring", 1.0), ("death ring", 0.25), ("amulet of loss", 0.25), ("gold ingot", 0.0025), ("golden sickle", 0.0025) )