class Merchant:
    def __init__(self, inventory: list):
        self._inventory = inventory
        self._name = "Tom Nook"
        self._objectType = "merchant"
        self._type = "shop"
        self._coin = 500
    
    def getType(self):
        return self._type

    def getObjectType(self):
        return self._objectType

    def getCoin(self):
        return self._coin

    #returns inventory
    def getInventory(self):
        return self._inventory

    #returns name
    def getName(self):
        return self._name

    def buy(self, item):
        self._inventory.append(item)


    def sell(self, item):
        self._inventory.remove(item)

        
    