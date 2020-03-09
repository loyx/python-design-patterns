"""implement adapter pattern using interface

这里使用简化的接口——协议
"""
import random
from typing import Union
from duck_and_turkey import *


class TurkeyToDuck:

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def fly(self):
        for _ in range(5):
            self.turkey.fly()

    def quack(self):
        self.turkey.gobble()


class DuckToTurkey:

    def __init__(self, duck: Duck):
        self.duck = duck
        self.distance = 0
        self.chance = random.randint(0, 5)

    def fly(self):
        if self.distance == self.chance:
            self.distance = 0
            self.chance = random.randint(0, 5)
            self.duck.fly()
        self.distance += 1
        assert self.distance < 5

    def gobble(self):
        self.duck.quack()


duck = Duck()
turkey = Turkey()

duck_turkey: Union[Turkey, DuckToTurkey] = DuckToTurkey(duck)
turkey_duck: Union[Duck, TurkeyToDuck] = TurkeyToDuck(turkey)

print("test turkey adapter")
test_Turkey_adapter(duck_turkey)
print("test duck adapter")
test_Duck_adapter(turkey_duck)
