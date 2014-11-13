elf_arcanist = genMonster("Elf Arcanist", (63, 6011), "an elf arcanist")
elf_arcanist.health(220, healthmax=220)
elf_arcanist.type("blood")
elf_arcanist.defense(armor=15, fire=0.5, earth=1, energy=0.8, ice=1, holy=1.1, death=0.8, physical=1, drown=1)
elf_arcanist.experience(175)
elf_arcanist.speed(230)
elf_arcanist.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=False, targetDistance=4, runOnHealth=0)
elf_arcanist.walkAround(energy=1, fire=1, poison=1)
elf_arcanist.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=0)
elf_arcanist.voices("I'll bring balance upon you!", "Vihil Ealuel", "For the Daughter of the Stars!", "Tha'shi Cenath", "Feel my wrath!")
elf_arcanist.regMelee(35)
elf_arcanist.loot( ("elvish talisman", 9.0), ("health potion", 4.5), ("blank rune", 18.75), ("elven astral observer", 8.75), ("bread", 13.5), (2148, 100, 45), ("melon", 23.0), ("scroll", 29.25), ("life crystal", 0.5), ("arrow", 9.5, 3), ("sling herb", 4.75), ("sandals", 1.0), ("inkwell", 1.25), ("wand of cosmic energy", 0.75), ("green tunic", 6.5), ("candlestick", 2.0), ("elven amulet", 1.75), ("strong mana potion", 3.75), ("holy orchid", 2.5, 3), ("grave flower", 1.0) )