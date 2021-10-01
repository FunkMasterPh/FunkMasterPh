from misc import *
from world_creator import *

door1.setIsOpen(False)
if not door1.getIsOpen():
    print("Closed")
else:
    print("Open")