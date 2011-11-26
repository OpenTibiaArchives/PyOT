
conjure = spell.Spell("Thunderstorm", "adori mas vis", icon=23, group=SUPPORT_GROUP)
conjure.require(mana=430, level=28, maglevel=0, soul=3, learned=0, vocations=(1, 5))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(2315, 3))

# Incomplete! Self target rune?
rune = spell.Rune(2315, icon=117, count=3, target=TARGET_TARGET, group=None)
rune.cooldowns(0, 2)
rune.require(mana=0, level=28, maglevel=0)
rune.targetEffect() # TODO
rune.effects() # TODO