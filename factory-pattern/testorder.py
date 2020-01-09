from PizzaStore import *

nyPizzaStore = NYStylePizzaStore()
nyPizzaStore.orderPizza("cheese")

"""对工厂模式的理解
无论是factory method 还是abstract factory都是为
了封装对象的创建，便于修改。从另一个角度看，各种concrete 
creator 之间的差别是他们有不同的属性，因此将它们划分为
不同的子类，将相同点抽象为父类，使用factory method满足
不同属性的要求。当不同的属性太多时，便组成一个抽象工厂。
但这一点也可以通过参数化的方法放在一个类里。使用工厂模式
可以减少类中的参数化代码，但在其他地方，如测试代码，便不可
避免的使用参数化代码
"""
