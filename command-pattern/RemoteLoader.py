from RemoteControl import RemoteControl
from Vendor import *
from Command import *

light = Light('living room')
ceilingFan = CeilingFan('living room')

lightOnCommand = LightOnCommand(light)
lightOffCommand = LightOffCommand(light)

ceilingFanHighCommand = CeilingFanHighCommand(ceilingFan)
ceilingFanLowCommand = CeilingFanLowCommand(ceilingFan)

remote = RemoteControl()
print(remote)

# remote.setOnCommand(0, lightOnCommand)
# remote.setOffCommand(0, lightOffCommand)
remote.setCommand(0, lightOnCommand, lightOffCommand)

remote.setOnCommand(3, ceilingFanHighCommand)
remote.setOnCommand(2, ceilingFanLowCommand)
print(remote)

remote.pushOnButton(0)
remote.pushOnButton(3)
remote.pushOnButton(2)
remote.pushOffButton(0)
print(remote)
remote.pushUndoButton()
print(remote)
remote.pushUndoButton()
print(remote)

macroCommand = MacroCommand([lightOnCommand, ceilingFanHighCommand])
remote.setOnCommand(1, macroCommand)
print(remote)
remote.pushOnButton(1)
print(remote)
remote.pushUndoButton()
print(remote)


