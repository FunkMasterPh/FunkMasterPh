from items_class import Armor

class LeatherHelmet(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 5
        self._value = 10
        self._type = "Leather_helmet"
        self._armor = 10

class IronHelmet(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 10
        self._value = 25
        self._type = "Iron_Helmet"
        self._armor = 15

class DaedricHelmet(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 7
        self._value = 100
        self._type = "Daedric_Helmet"
        self._armor = 30

class LeatherBreastplate(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 12
        self._value = 15
        self._type = "Leather_Breastplate"
        self._armor = 20

class IronBreastplate(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 25
        self._value = 35
        self._type = "Iron_Breastplate"
        self._armor = 35

class DaedricBreastplate(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 15
        self._value = 150
        self._type = "Daedric_Breastplate"
        self._armor = 63

class LeatherLeggings(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 10
        self._value = 13
        self._type = "Leather_Pantalones"
        self._armor = 16

class IronLeggings(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 22
        self._value = 30
        self._type = "Iron_Longjohns"
        self._armor = 25

class DaedricLeggings(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 15
        self._value = 120
        self._type = "Daedric_Briefs"
        self._armor = 42

class LeatherBoots(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 10
        self._value = 13
        self._type = "Leather_Shoes"
        self._armor = 16

class IronBoots(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 15
        self._value = 13
        self._type = "Iron_Boots"
        self._armor = 16

class DaedricBoots(Armor):
    def __init__(self):
        super().__init__()
        self._weight = 10
        self._value = 13
        self._type = "Daedric_Socks_of_massive_handsomeness"
        self._armor = 25

