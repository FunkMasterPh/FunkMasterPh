from monster_class import Monster
import items_class as item
import weapons
import misc

class Goblin(Monster):
    def __init__(self, inventory: list):
        super().__init__(self)
        self._hp = 10
        self._str = 3
        self._dex = 1
        self._type = "Goblin"
        self._desc = "A goblin! It's small, ugly and hungry. Better watch out!"
        self._corpseDesc = "The body of a dead goblin."
        self._inventory = inventory
        self._giveXP = 25
    
class Troll(Monster):
    def __init__(self, inventory: list):
        super().__init__(self)
        self._hp = 100
        self._str = 10
        self._dex = 1
        self._type = "Troll"
        self._desc = "Disfigured and smells funky"
        self._corpseDesc = "The body of a dead troll."
        self._inventory = inventory
        self._giveXP = 100
    
class Orc(Monster):
    def __init__(self, inventory: list):
        super().__init__(self)
        self._hp = 60
        self._str = 20
        self._dex = 10
        self._type = "Orc"
        self._desc = "Humanoid with insane strength and durability!"
        self._corpseDesc = "The body of a dead orc."
        self._inventory = inventory
        self._giveXP = 25

class Slime(Monster):
    def __init__(self, inventory: list):
        super().__init__(self)
        self._hp = 5
        self._str = 1
        self._dex = 2
        self._type = "Slime"
        self._desc = "Small and slippery and comes in large numbers!"
        self._corpseDesc = "The body of a dead Slime."
        self._inventory = inventory
        self._giveXP = 5

class Skeleton(Monster):
    def __init__(self, inventory: list):
        super().__init__(self)
        self._hp = 35
        self._str = 9
        self._dex = 1
        self._type = "Skeleton"
        self._desc = "Walking set of bones!"
        self._corpseDesc = "The body of a dead Skelly."
        self._inventory = inventory
        self._giveXP = 20

class TreasureGnome(Monster):
    def __init__(self, inventory: list):
        super().__init__(self)
        self._hp = 100
        self._str = 1
        self._dex = 40
        self._type = "Gnome"
        self._desc = "Tiny creature running around with a bag of goodies!"
        self._corpseDesc = "The body of a dead gnome."
        self._inventory = inventory
        self._giveXP = 100