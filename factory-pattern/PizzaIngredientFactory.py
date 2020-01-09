from Ingredient import *


class PizzaIngredientFactory(ABC):
    """abstract factory"""

    @abstractmethod
    def createDough(self):
        pass

    @abstractmethod
    def createSauce(self):
        pass

    @abstractmethod
    def createCheese(self):
        pass

    @abstractmethod
    def createVeggies(self):
        pass

    @abstractmethod
    def createPepperoni(self):
        pass

    @abstractmethod
    def createClam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSauce()

    def createCheese(self):
        return ReggianoCheese()

    def createVeggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def createPepperoni(self):
        return SlicePepperoni()

    def createClam(self):
        return FreshClam()
