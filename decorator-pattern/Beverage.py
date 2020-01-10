from abc import ABC, abstractmethod
import keras


class Beverage(ABC):

    def __init__(self):
        self.description = "Unknown Beverage"

    def getDescription(self):
        return self.description

    @abstractmethod
    def cost(self):
        """beverage cost"""


class CondimentDecorator(Beverage, ABC):
    """decorator interface

    事实上python是动态类型并不需要该接口
    """

    @abstractmethod
    def getDescription(self):
        pass


'''concrete beverages'''


class Espresso(Beverage):

    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):

    def __init__(self):
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self):
        return 0.89


'''concrete decorators

python 中装饰器的作用与设计模式中的装饰器模式类似，但实现上并不同。
装饰器并不能代替装饰器模式
'''


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()

    def __call__(self, *args, **kwargs):
        return self


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"

    def cost(self):
        return .10 + self.beverage.cost()


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Soy"

    def cost(self):
        return .15 + self.beverage.cost()
