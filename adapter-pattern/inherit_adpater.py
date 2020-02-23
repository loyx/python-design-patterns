"""implement adapter pattern using inherit"""

import random
from duck_and_turkey import *


class DuckToTurkey(Duck, Turkey):
    """ smart adapter """

    def __init__(self):
        self.chance = random.randint(0, 5)
        self.distance = 0

    def fly(self):
        if self.distance == self.chance:
            self.distance = 0
            self.chance = random.randint(0, 5)
            Duck.fly()
            return
        self.distance += 1
        assert self.distance < 5

    def gobble(self):
        self.quack()


class TurkeyToDuck(Duck, Turkey):

    def fly(self):
        for _ in range(5):
            Turkey.fly()
            # 这是多继承Python中寻找超类method的方法
            # 还可以改变__mro__中超类顺序，从而用super().fly()

    def quack(self):
        self.gobble()


turkey_duck = TurkeyToDuck()
print("test duck adapter:")
test_Duck_adapter(turkey_duck)

duck_turkey = DuckToTurkey()
print("test turkey adapter:")
test_Turkey_adapter(duck_turkey)
