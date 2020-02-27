""" template pattern """
from abc import ABC, abstractmethod

""" 这个模式看起来只是在减少duplicated code 
应用在实际时， 说不定需要改的更多， 对个人开发者来说有利有弊
但对于框架作者来说， 这可以保证使用者有可以期待的行为， 保证了框架稳定性。
"""


class CaffeineBeverage(ABC):

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.hook():
            self.addCondiments()

    @staticmethod
    def boilWater():
        print("Boiling water...")

    @staticmethod
    def pourInCup():
        print("Pouring into cup...")

    @abstractmethod
    def brew(self):
        """ primitive operation """

    @abstractmethod
    def addCondiments(self):
        """ primitive operation """

    @staticmethod
    def hook():
        """ hook function """
        return True


class Coffee(CaffeineBeverage):

    def brew(self):
        print("Dripping Coffee through filter")

    def addCondiments(self):
        print("Adding sugar and milk")

    def hook(self):
        answer = input("Would you like add sugar and milk with you coffee? (Y/n):")
        if answer.startswith('n') or answer.startswith('N'):
            return False
        return True


if __name__ == '__main__':
    coffee = Coffee()
    coffee.prepareRecipe()
