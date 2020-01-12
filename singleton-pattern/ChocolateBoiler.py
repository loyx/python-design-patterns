class ChocolateBoiler:

    unique_instance = None

    @staticmethod
    def getInstance():
        if ChocolateBoiler.unique_instance is None:
            ChocolateBoiler.unique_instance = ChocolateBoiler()
        return ChocolateBoiler.unique_instance

    def __init__(self):
        self.__empty = True
        self.__boiled = False

    def fill(self):
        if self.isEmpty():
            self.__empty = False
            self.__boiled = False
            '''fill the boiler'''

    def drain(self):
        if not self.isEmpty() and self.isBoiled():
            '''drain the boiler'''
            self.__empty = True

    def boil(self):
        if not self.isEmpty() and not self.isBoiled():
            '''bring the contents to a boil'''
            self.__boiled = True

    def isEmpty(self):
        return self.__empty

    def isBoiled(self):
        return self.__boiled
