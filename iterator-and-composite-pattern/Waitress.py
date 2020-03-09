from MenuComponent import *

pancakeHouseMenu = Menu("PANCAKE HOUSE MENU", "Breakfast")
dinerMenu = Menu("DINER MENU", "Lunch")
cafeMenu = Menu("CAFE MENU", "Dinner")
dessertMenu = Menu("DESSERT MENU", "Dessert of course!")

allMenus = Menu("ALL MENUS", "All menus combined")

allMenus.add(pancakeHouseMenu)
allMenus.add(dinerMenu)
allMenus.add(cafeMenu)

pancakeHouseMenu.add(MenuItem("pancakeItem1", "this is a pancakeItem", True, 5))
pancakeHouseMenu.add(MenuItem("pancakeItem2", "this is a pancakeItem", False, 8))
pancakeHouseMenu.add(MenuItem("pancakeItem3", "this is a pancakeItem", False, .5))

dinerMenu.add(MenuItem("dinerItem1", "this is a dinerItem", False, 10))
dinerMenu.add(MenuItem("dinerItem2", "this is a dinerItem", True, 12))
dinerMenu.add(dessertMenu)
dinerMenu.add(MenuItem("dinerItem3", "this is a dinerItem", False, 14))

dessertMenu.add(MenuItem("dessertItem1", "this is a dessertItem", True, 4))
dessertMenu.add(MenuItem("dessertItem2", "this is a dessertItem", True, 3))
dessertMenu.add(MenuItem("dessertItem3", "this is a dessertItem", True, 1))

cafeMenu.add(MenuItem("cafeItem1", "this is a cafeItem", True, 8))
cafeMenu.add(MenuItem("cafeItem2", "this is a cafeItem", True, 10))
cafeMenu.add(MenuItem("cafeItem3", "this is a cafeItem", True, 8.8))

allMenus.print()

print("\nVEGETARIAN MENU")
print("---")

menuItem: MenuItem
for menuItem in allMenus:
    if menuItem.isVegetarian():
        menuItem.print()
