jeweler = genNPC("Jeweler", (130, 39, 122, 125, 37, 0, 2212))
jeweler.setWalkable(False)
#buy,sell
shop = jeweler.module('shop')
shop.offer('white pearl', 320, 160)
shop.offer('black pearl',560, 280)
shop.offer('small diamond',600, 300)
shop.offer('small sapphire',500, 250)
shop.offer('small ruby',500, 250)
shop.offer('small emerald',500, 250)
shop.offer('small amethyst', 400, 200)
shop.offer('ruby necklace', 3560)
shop.offer('wedding ring', 990, 100)
shop.offer('golden amulet', 6600)
shop.offer('golden goblet', 5000)
shop.offer('silver goblet', 3000)
shop.offer('bronze goblet', 2000)
shop.offer('small topaz', 0, 200)
shop.offer('gold ingot', 0, 5000 )