
conjure = spell.Spell("Poisoned Arrow", "exevo con pox", icon=48, group=SUPPORT_GROUP)
conjure.require(mana=130, level=16, maglevel=0, soul=2, learned=0, vocations=(3, 7))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(2545, 7))