dragon_lord = game.monster.genMonster("Dragon Lord", (39, 5984), "a dragon lord")
dragon_lord.setHealth(1900)
dragon_lord.bloodType(color="blood")
dragon_lord.setDefense(armor=37, fire=0, earth=0.2, energy=0.8, ice=1.1, holy=1, death=1, physical=1, drown=1)
dragon_lord.setExperience(2100)
dragon_lord.setSpeed(240)
dragon_lord.setBehavior(summonable=0, hostile=1, illusionable=1, convinceable=0, pushable=0, pushItems=1, pushCreatures=1, targetDistance=1, runOnHealth=300)
dragon_lord.walkAround(energy=0, fire=0, poison=0)
dragon_lord.setImmunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
dragon_lord.voices("YOU WILL BURN!", "ZCHHHHHHH")
dragon_lord.loot( (2148, 100, 245), ("dragon ham", 77.25), ("green mushroom", 12.0), ("small sapphire", 5.0), ("red dragon scale", 2.0), ("power bolt", 26.0, 7), ("energy ring", 5.0), ("dragon slayer", 0.0025), ("royal spear", 18.0, 3), ("book", 9.0), ("golden mug", 3.0), ("life crystal", 0.5), ("royal helmet", 0.25), ("tower shield", 0.25), ("strong health potion", 1.0), ("red dragon leather", 1.0), ("fire sword", 0.25), ("strange helmet", 0.5), ("dragon scale mail", 0.0025), ("dragon lord trophy", 0.0025) )

dfwave = spell.Spell("drag fwave", target=TARGET_AREA)
dfwave.area(AREA_WAVE8)
dfwave.element(FIRE)
dfwave.effects(area=EFFECT_HITBYFIRE)
 
dlfbomb = spell.Spell("drag fbomb", target=TARGET_TARGETONLY)
dlfbomb.area(AREA_CIRCLE3)
dlfbomb.element(callback=spell.field(1492))
dlfbomb.effects(area=EFFECT_HITBYFIRE, shoot=ANIMATION_FIRE) 
 
dragon_lord.regMelee(220)
dragon_lord.regTargetSpell("drag fbomb", check=game.monster.chance(20))
dragon_lord.regTargetSpell("drag fwave", 150, 250, check=game.monster.chance(20))
dragon_lord.regTargetSpell(2304, 100, 200, check=game.monster.chance(20)) #gfb

dragon_lord.regTargetSpell("Light Heaing", 25, 55, check=game.monster.chance(18))