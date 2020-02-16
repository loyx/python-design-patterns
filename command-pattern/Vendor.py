class Light:

    def __init__(self, location):
        self.location = location

    @staticmethod
    def on():
        print("Light on")

    @staticmethod
    def off():
        print("Light off")


class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        self.location = location
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH
        print("CeilingFan set to high")

    def medium(self):
        self.speed = self.MEDIUM
        print("CeilingFan set to medium")

    def low(self):
        self.speed = self.LOW
        print("CeilingFan set to low")

    def off(self):
        self.speed = self.OFF
        print("CeilingFan turn off")
