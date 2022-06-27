# FANTASY GAME CODE
print('INVENTORY:')

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(stuff):
    total = 0
    for k, v in stuff.items():
        print(str(v)+' '+ k)
        total += v
    print("Total number of items: " + str(total))

displayInventory(stuff)

#----------------------------------------------------
# DRAGON LOOT CODE

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print('INVENTORY:')

def addToInventory(previousInventory, addedItems):
    for item in addedItems:
        previousInventory.setdefault(item, 0) #this adds a (defaulted to zero value) key to the stuff dict if it's not already there
        previousInventory[item] += 1  #and this increases that value by one, each time that item appears in the loot list
    return previousInventory


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
