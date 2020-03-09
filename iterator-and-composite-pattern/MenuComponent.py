""" composite pattern and Pythonic iterator"""


class MenuItem:
    dis_format = "  {Item.name}{{}}, {Item.price}￥\n    --{Item.description}"

    def __init__(self, name, description, vegetarian, price):
        self.name: str = name
        self.description = description
        self.vegetarian = vegetarian
        self.price: float = price

    def print(self):
        print(self.dis_format.format(Item=self).format(' v' if self.isVegetarian() else ''))

    def isVegetarian(self):
        return self.vegetarian


class Menu:

    def __init__(self, name="Menu", description=None):
        self.menuComponents: list = []
        self.name: str = name
        self.description: str = description

    def print(self):
        print("\n{0.name}, {0.description}".format(self))
        print('-------------------------')

        """ python 中的for会自动处理iterable对象 """
        for item in self.menuComponents:
            item.print()
        print('*************************\n')

    def add(self, menu_component):
        self.menuComponents.append(menu_component)

    def remove(self, menu_component):
        self.menuComponents.remove(menu_component)

    """ 这两特殊方法实现了序列协议, 则对于python来说， 它就是可迭代对象
        实际只要实现__getitem__ python 就会尝试迭代它。
    """
    def __getitem__(self, item):
        return self.menuComponents[item]

    def __len__(self):
        return len(self.menuComponents)

    """ 使用生成器函数实现python版迭代器，传统的迭代器都可以用生成器函数替代
    """
    def __iter__(self):
        for component in self.menuComponents:
            if isinstance(component, MenuItem):
                yield component
            else:
                yield from iter(component)
        return

