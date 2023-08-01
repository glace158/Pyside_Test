import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject, Signal, Slot

app = QApplication(sys.argv)

# define a new slot that receives a C 'int' or a 'str'
# and has 'saySomething' as its name
@Slot(int)
@Slot(str)
def say_something(stuff):
    print(stuff)

class Communicate(QObject):
    # create two new signals on the fly: one will handle
    # int type, the other will handle strings
    speak = Signal((int,), (str,))

someone = Communicate()
# connect signal and slot. As 'int' is the default
# we have to specify the str when connecting the
# second signal
someone.speak.connect(say_something)
someone.speak[str].connect(say_something)

# emit 'speak' signal with different arguments.
# we have to specify the str as int is the default
someone.speak.emit(10)
someone.speak[str].emit("Hello everybody!")