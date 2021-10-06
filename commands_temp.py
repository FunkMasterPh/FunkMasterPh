
def examine(toLookAt, currentRoom):
    """takes user input and examines thing depending on input"""
    if findObjectInRoom(currentRoom, toLookAt):
        item = findObjectInRoom(currentRoom,toLookAt)
        if item.getObjectType() == MONSTER:
            examineMonster(item)
        elif item.getObjectType() == ITEM:
            print(item.getDesc())
        elif item.getObjectType() == CHEST:
            print(item.getDesc())
            if item.getInventory() and item.getIsOpen():
                print("It contains:")
                printInventory(item)
        elif item.getObjectType() == MERCHANT:
            print("He has these items for sale: ")
            for thing in item.getInventory():
                print(f"{thing.getType().title()} for {int(thing.getValue() * 1.2)} coins.")
                
    if findObjectInPlayer(player, toLookAt):
        item = findObjectInPlayer(player, toLookAt)
        print(item.getDesc())
    
    elif not findObjectInPlayer(player, toLookAt) and not findObjectInRoom(currentRoom, toLookAt):
        print("That doesn't exist.") 