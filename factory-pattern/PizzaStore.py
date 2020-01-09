from abc import ABC, abstractmethod
from PizzaIngredientFactory import *
from Pizza import *


class PizzaStore(ABC):

    def orderPizza(self, pizza_type):
        pizza = self.createPizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

    @abstractmethod
    def createPizza(self, item):
        """factory method"""


class NYStylePizzaStore(PizzaStore):

    def createPizza(self, item):
        """implemented factory method"""
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()
        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.setName("New York Style Cheese Pizza")
        elif item == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.setName("New York Style Clam Pizza")
        # elif ... other pizza
        return pizza


class ChicagoStylePizzaStore(PizzaStore):

    def createPizza(self, item):
        pass
