from items_class import Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 10
        self._value = 20
        self._type = "Sword"
        self._desc = "Excalibur"
        self._damage = 10

class Dagger(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 5
        self._value = 15
        self._type = "Dagger"
        self._damage = 4

class Whip(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 2
        self._value = 6
        self._type = "Whip. "
        self._damage = 1

class Club(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 9
        self._value = 10
        self._type = "Club"
        self._damage = 7

class Mace(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 15
        self._value = 25
        self._type = "Mace. "
        self._damage = 18

class Axe(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 10
        self._value = 20
        self._type = "Axe"
        self._desc = "An axe with a wooden handle"
        self._damage = 100

class Crossbow(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 16
        self._value = 15
        self._type = "Crossbow"
        self._damage = 15

class Boomerang(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 7
        self._value = 14
        self._type = "A bent piece of wood"
        self._damage = 5

class Rock(Weapon):
    def __init__(self):
        super().__init__()
        self._weight = 4
        self._value = 1
        self._type = "A rock. nothing more, nothing less"
        self._damage = 2