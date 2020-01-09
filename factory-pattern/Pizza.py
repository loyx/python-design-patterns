from abc import ABC, abstractmethod


class Pizza(ABC):

    def __init__(self):
        self.name = ""
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    @abstractmethod
    def prepare(self):
        """abstract factory"""

    def bake(self):
        print("Bake {} for 25 minutes at 350".format(self.name))

    def cut(self):
        print("Cutting the {} into diagonal slices".format(self.name))

    def box(self):
        print("Place {} in official PizzaStore box".format(self.name))

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class CheesePizza(Pizza):

    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing %s" % self.name)
        self.dough = self.ingredient_factory.createDough()
        self.sauce = self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createCheese()


class ClamPizza(Pizza):

    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing %s" % self.name)
        self.dough = self.ingredient_factory.createDough()
        self.sauce = self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createCheese()
        self.clam = self.ingredient_factory.createClam()
