larva = genMonster("Larva", (82, 6023), "a larva")
larva.setHealth(70, healthmax=70)
larva.bloodType(color="slime")
larva.setDefense(armor=4, fire=1.1, earth=0, energy=0.9, ice=1.05, holy=1, death=1, physical=1, drown=1)
larva.setExperience(44)
larva.setSpeed(135)
larva.setBehavior(summonable=355, hostile=1, illusionable=1, convinceable=0, pushable=1, pushItems=0, pushCreatures=0, targetDistance=1, runOnHealth=0)
larva.walkAround(energy=1, fire=1, poison=0)
larva.setImmunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
larva.regMelee(35)#poison 1p/turn
larva.loot( ("meat", 14.25), (2148, 100, 15) )