instant = spell.Spell("Ethereal Spear", "exori con", icon=111, group=ATTACK_GROUP)
instant.require(mana=25, level=23, maglevel=0, learned=0, vocations=(3, 7))
instant.cooldowns(2, 2)
instant.targetEffect(callback=spell.damage(3.184, 5.59, 0, 5, HOLY)) #UNKNOWN (X, X, 0, 5)
#PHYSICAL BASED?
instant.effects() # TODO