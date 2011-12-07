conjure = spell.Spell("Great Fireball", "adori mas flam", icon=23, group=SUPPORT_GROUP)
conjure.require(mana=530, level=30, maglevel=0, soul=3, learned=0, vocations=(1, 5))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(2304, 3))

# Incomplete! Field rune.
rune = spell.Rune(2304, icon=16, count=3, target=TARGET_AREA, group=ATTACK_GROUP)
rune.cooldowns(0, 2)
rune.area(AREA_CIRCLE3)
rune.require(mana=0, level=30, maglevel=0)
rune.targetEffect(callback=spell.damage(1.2, 2.85, 20, 35, FIRE))
rune.effects() # TODO