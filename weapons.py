from items_class import Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 10
        self._value = 10
        self._type = "sword"
        self._desc = "Excalibur"
        self._damage = 10

class Axe(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 10
        self._value = 20
        self._type = "axe"
        self._desc = "An axe with a wooden handle"
        self._damage = 100
