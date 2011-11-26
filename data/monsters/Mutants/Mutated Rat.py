mutated_rat = game.monster.genMonster("Mutated Rat", (305, 9871), "a mutated rat")
mutated_rat.setHealth(550)
mutated_rat.bloodType(color="blood")
mutated_rat.setDefense(armor=29, fire=1.1, earth=0, energy=1, ice=1, holy=0.9, death=0, physical=1, drown=0)
mutated_rat.setExperience(450)
mutated_rat.setSpeed(245)
mutated_rat.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
mutated_rat.walkAround(energy=0, fire=0, poison=0)
mutated_rat.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
mutated_rat.voices("Grrrrrrrrrrrrrr!", "Fcccccchhhhhh")
mutated_rat.regMelee(155) #poisons you 5 hp/turn
mutated_rat.loot( (2235, 1.0), ("skull", 20.5), ("stone herb", 4.75), ("halberd", 3.0), ("mutated rat tail", 4.0), (2148, 100, 130), ("plate shield", 4.0), ("spellbook of enlightenment", 0.5), ("health potion", 0.5), ("green mushroom", 1.5), ("stealth ring", 0.5), ("tower shield", 0.0025) )