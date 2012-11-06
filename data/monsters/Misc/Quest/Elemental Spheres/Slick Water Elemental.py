slick_water_elemental = genMonster("Slick Water Elemental", (286, 8965), "a slick water elemental")
slick_water_elemental.setHealth(550, healthmax=550)
slick_water_elemental.bloodType(color="undead")
slick_water_elemental.setDefense(armor=39, fire=0, earth=0, energy=1, ice=0, holy=0.4, death=0.5, physical=0.3, drown=1)
slick_water_elemental.setExperience(450)
slick_water_elemental.setSpeed(280)
slick_water_elemental.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=0)
slick_water_elemental.walkAround(energy=1, fire=0, poison=0)
slick_water_elemental.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
slick_water_elemental.voices("BLUUUUB", "SPLISH SPLASH")
slick_water_elemental.regMelee(175)
slick_water_elemental.loot( (2148, 100, 126), ("shiver arrow", 5.25, 3), ("iced soil", 6.0) )