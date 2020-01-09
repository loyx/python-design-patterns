from abc import ABC, abstractmethod


class Dough(ABC):
    """Dough interface"""


class ThinCrustDough(Dough):

    def __init__(self):
        self.name = "Thin Crust Dough"


class Sauce(ABC):
    """Sauce interface"""


class MarinaraSauce(Sauce):

    def __init__(self):
        self.name = "Marinara Sauce"


class Cheese(ABC):
    """Cheese interface"""


class ReggianoCheese(Cheese):

    def __init__(self):
        self.name = "Reggiano Cheese"


class Veggies(ABC):
    """Veggies interface"""


class Garlic(Veggies):

    def __init__(self):
        self.name = "Garlic"


class Onion(Veggies):

    def __init__(self):
        self.name = "Onion"


class Mushroom(Veggies):

    def __init__(self):
        self.name = "Mushroom"


class RedPepper(Veggies):

    def __init__(self):
        self.name = "RedPepper"


class Pepperoni(ABC):
    """Pepperoni interface"""


class SlicePepperoni(Pepperoni):

    def __init__(self):
        self.name = "Slice Pepperoni"


class Clam(ABC):
    """Clam interface"""


class FreshClam(Clam):

    def __init__(self):
        self.name = "Fresh Clam"

# JAVA 真烦，用python写JAVA我也是够蠢的...
