from items_class import Misc

class Torch(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 3
        self._value = 5
        self._type = "torch"
        self._desc ="A stick on fire. "
        self._isOn = False
    
    #returns on/off status of torch
    def getOn(self):
        return self._isOn
    
    #sets torch status to on
    def setOnOff(self, arg):
        self._isOn = arg

class Monocle(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 1
        self._value = 25
        self._type = "Monocle"
        self._desc ="A circular piece of glass from an era long ago. "

class Ladder(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 20
        self._value = 12
        self._type = "Ladder"
        self._desc ="Might be able to use this for something. "

class Key(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 2
        self._value = 50
        self._type = "Key"
        self._desc ="Special looking key for a special type of door. "

class OldMap(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 1
        self._value = 8
        self._type = "Map"
        self._desc ="Dusty piece of cloth and what looks like the remaining ink from what used to be a map. "

class Diamond(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 5
        self._value = 200
        self._type = "Diamond"
        self._desc ="Shiny jewel, looks expensive. "

class Emerald(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 5
        self._value = 150
        self._type = "Emerald"
        self._desc ="Shiny jewel, looks expensive. "

class Ruby(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 5
        self._value = 150
        self._type = "Ruby"
        self._desc ="Shiny jewel, looks expensive. "

class Sapphire(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 5
        self._value = 150
        self._type = "Sapphire"
        self._desc ="Shiny jewel, looks expensive. "

class Rolex(Misc):
    def __init__(self):
        super().__init__()
        self._weight = 5
        self._value = 500
        self._type = "Rolex"
        self._desc ="Golden Watch. "