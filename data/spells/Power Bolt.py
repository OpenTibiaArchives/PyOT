
conjure = spell.Spell("Power Bolt", "exevo con vis", icon=23, group=SUPPORT_GROUP)
conjure.require(mana=800, level=59, maglevel=0, soul=3, learned=0, vocations=(7,))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(2547, 10))