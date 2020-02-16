from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        """command"""

    @abstractmethod
    def undo(self):
        """support undo"""

    def __repr__(self):
        return type(self).__name__


class NoCommand(Command):
    """null object"""

    def execute(self):
        """do nothing"""

    def undo(self):
        """do nothing"""


class LightOnCommand(Command):

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.on()

    def undo(self):
        self.receiver.off()


class LightOffCommand(Command):

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.off()

    def undo(self):
        self.receiver.on()


class CeilingFanHighCommand(Command):

    def __init__(self, receiver):
        self.receiver = receiver
        self.preSpeed = -1  # 开始无preSpeed

    def execute(self):
        self.preSpeed = self.receiver.speed
        self.receiver.high()

    def undo(self):
        if self.preSpeed == self.receiver.OFF:
            self.receiver.off()
        elif self.preSpeed == self.receiver.LOW:
            self.receiver.low()
        elif self.preSpeed == self.receiver.MEDIUM:
            self.receiver.medium()
        # no need for high


class CeilingFanLowCommand(Command):

    def __init__(self, receiver):
        self.receiver = receiver
        self.preSeed = -1

    def execute(self):
        self.preSeed = self.receiver.speed
        self.receiver.low()

    def undo(self):
        if self.preSeed == self.receiver.OFF:
            self.receiver.off()
        elif self.preSeed == self.receiver.MEDIUM:
            self.receiver.medium()
        elif self.preSeed == self.receiver.HIGH:
            self.receiver.high()
        # no need for low


class MacroCommand(Command):

    def __init__(self, commands):
        self.commands = list(commands)

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()
