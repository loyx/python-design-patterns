from Command import NoCommand

"""RemoteControl play invoker"""


class RemoteControl:

    def __init__(self, slot_num=4, undo_deep=3):
        self.onCommands = []
        self.offCommands = []
        self.undoCommands = []  # for more undo
        for _ in range(slot_num):
            self.onCommands.append(NoCommand())
            self.offCommands.append(NoCommand())

    def setOnCommand(self, slot, command):
        self.onCommands[slot] = command

    def setOffCommand(self, slot, command):
        self.offCommands[slot] = command

    def setCommand(self, slot, on_command, off_command):
        self.setOnCommand(slot, on_command)
        self.setOffCommand(slot, off_command)

    def pushOnButton(self, slot):
        command = self.onCommands[slot]
        command.execute()
        self.undoCommands.append(command)

    def pushOffButton(self, slot):
        command = self.offCommands[slot]
        command.execute()
        self.undoCommands.append(command)

    def pushUndoButton(self):
        if len(self.undoCommands) > 0:
            command = self.undoCommands.pop()
            command.undo()

    def __repr__(self):
        line_item = '{:^5}|{:^40}|{:^40}|\n'
        ret = line_item.format('slots', 'OnCommands', 'OffCommands')
        for index, (on, off) in enumerate(zip(self.onCommands, self.offCommands)):
            ret += line_item.format(index, type(on).__name__, type(off).__name__)
        ret += 'undoCommandList:{}\n'.format(self.undoCommands)
        return ret
