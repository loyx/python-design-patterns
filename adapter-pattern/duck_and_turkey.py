"""target and client class"""


class Duck:

    @staticmethod
    def fly():
        print("Duck: I'm flying!")

    @staticmethod
    def quack():
        print("Duck: Quack!")


class Turkey:

    @staticmethod
    def fly():
        print("Turkey: I'm flying a short distance!")

    @staticmethod
    def gobble():
        print("Turkey: Gobble gobble!")


def test_Duck_adapter(duck: Duck):
    duck.fly()
    duck.quack()


def test_Turkey_adapter(turkey: Turkey):
    turkey.fly()
    turkey.gobble()
