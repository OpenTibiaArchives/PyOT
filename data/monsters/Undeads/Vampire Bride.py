vampire_bride = game.monster.genMonster("Vampire Bride", (312, 9660), "a vampire bride")
vampire_bride.setHealth(1200)
vampire_bride.bloodType(color="blood")
vampire_bride.setDefense(armor=60, fire=1.1, earth=0.8, energy=0.9, ice=0.8, holy=1.1, death=0, physical=1, drown=0.9)
vampire_bride.setExperience(1050)
vampire_bride.setSpeed(180)
vampire_bride.setBehavior(summonable=0, hostile=1, illusionable=0, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
vampire_bride.walkAround(energy=1, fire=1, poison=1)#incorrect?
vampire_bride.setImmunity(paralyze=0, invisible=1, lifedrain=0, drunk=1)
vampire_bride.voices("Kneel before your Mistress!", "Dead is the new alive.", "Come, let me kiss you, darling. Oh wait, I meant kill.", "Enjoy the pain - I know you love it.", "Are you suffering nicely enough?")
vampire_bride.regMelee(200)
vampire_bride.loot( ("emerald bangle", 1.0), (5669, 0.25), ("hibiscus dress", 0.75), ("boots of haste", 0.25), ("leather whip", 0.0025), ("velvet tapestry", 1.0), ("small diamond", 1.75, 2), ("rusty armor", 0.75), ("platinum coin", 9.75), ("strong mana potion", 9.75), ("moonlight rod", 4.75), ("blood preservation", 4.5), ("strong health potion", 4.75), (2148, 100, 149), ("vampire teeth", 9.75), ("flower bouquet", 0.25), ("blood goblet", 0.0025) )