spectre = genMonster("Spectre", (235, 6348), "a spectre")
spectre.setHealth(1350)
spectre.bloodType("undead")
spectre.setDefense(armor=44, fire=1.08, earth=0, energy=1.08, ice=0.99, holy=1, death=0, physical=0.1, drown=0)
spectre.setExperience(2100)
spectre.setSpeed(250)
spectre.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
spectre.walkAround(energy=1, fire=1, poison=0)
spectre.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
spectre.voices("Revenge ... is so ... sweet.", "Life...force! Feed me your... lifeforce", "Mor... tals!")
spectre.regMelee(270)
spectre.loot( ("shiny stone", 1.0), ("platinum coin", 14.0, 7), ("wand of cosmic energy", 10.0), ("soul orb", 6.5), ("demonic essence", 6.0, 3), ("silver brooch", 0.75), ("blank rune", 44.25, 2), (2148, 100, 297), ("white piece of cloth", 3.75), ("lyre", 10.5), ("great mana potion", 1.0), ("relic sword", 0.75), ("shadow sceptre", 0.25), ("death ring", 0.25), ("stealth ring", 0.25), ("demonbone amulet", 0.0025) )