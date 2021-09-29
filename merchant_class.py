class Merchant:
    def __init__(self, name):
        self._inventory = []
        self._name = "Tom Nook"
    
    def getInventory(self):

        return self.inventory

    def getName(self):

        return self._name
    
    def sell(self, item):

        self._inventory.remove(item)

    def purchase(self, item):

        self._inventory.append(item)

        
    