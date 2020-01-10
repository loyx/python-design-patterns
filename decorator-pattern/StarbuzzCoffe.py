from Beverage import Espresso, HouseBlend, Whip, Mocha, Soy

beverage1 = Espresso()
print(beverage1.getDescription() + " $" + str(beverage1.cost()))

beverage2 = HouseBlend()
beverage2 = Whip(beverage2)
beverage2 = Mocha(beverage2)
beverage2 = Soy(beverage2)
print(beverage2.getDescription() + " $" + str(beverage2.cost()))
