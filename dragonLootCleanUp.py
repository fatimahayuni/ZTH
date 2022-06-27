# FANTASY GAME INVENTORY CODE
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(stuff):
    total = 0
    for k, v in stuff.items():
        print(str(v) + ' ' + k)
        total += v
    print("Total number of items: " + str(total))


displayInventory(stuff)

#---------------------------------------------------------------------------
# DRAGON LOOT CODE
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] #list -> tuple
inv = {'gold coin': 42, 'rope': 1}
count = {}

for i in tuple(dragonLoot): #chunk A
    count.setdefault(i, 0)
    count[i] = count[i] + 1

inv3 = {}
for d in count, inv:
    total = 0
    for k, v in d.items():  #chunk B
        inv3[k] = inv3.get(k, 0) + v
        total += v
#how to combine chunk A and chunk B together? check answer. 

print('Inventory:')
print(str(inv3.get('gold coin', 0)) + ' gold coins')
print(str(inv3.get('dagger', 0)) + ' dagger')
print(str(inv3.get('ruby', 0)) + ' ruby')
print(str(inv3.get('rope', 0)) + ' rope')
print("Total number of items: "+str(total))
