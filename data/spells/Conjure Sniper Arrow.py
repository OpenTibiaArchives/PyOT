
conjure = spell.Spell("Conjure Sniper Arrow", "exevo con hur", icon=23, group=SUPPORT_GROUP)
conjure.require(mana=160, level=24, maglevel=0, soul=3, learned=0, vocations=(3, 7))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(7364, 5))