class Merchant:
    def __init__(self, name):
        self._inventory = []
        self._name = "Tom Nook"
    
    #returns inventory
    def getInventory(self):

        return self.inventory
    #returns name
    def getName(self):

        return self._name
    
    #method for selling items to player
    def sell(self, item):

        self._inventory.remove(item)
    
    #method for buying items from player
    def purchase(self, item):

        self._inventory.append(item)

        
    