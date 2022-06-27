dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] #list -> tuple
inv = {'gold coin': 42, 'rope': 1}

# 1. Convert List to Tuples using using tuple() method. Then convert tuple 
# list to dictionary using setdefault() method and for loop to count each item. 
count = {}

for i in tuple(dragonLoot):
    count.setdefault(i, 0)
    count[i] = count[i] + 1

# 2. Now dah dapat list converted to dictionary), what next?
# Print out dragonLoot and Inv in one new dictionary. How to do
# that? Refer to Dictionaries notes. Update. The answer is in nested for loops. 
'''
dragonLoot = {'gold coin': 3, 'dagger': 1, 'ruby': 1}
inv = {'gold coin': 42, 'rope': 1}
'''
inv3 = {}
for d in count, inv:
    total = 0
    for k, v in d.items():
        inv3[k] = inv3.get(k, 0) + v
        total += v

# 3: So now I know how to convert list to dictionary. I know how to print the
# added items together. So what next? Print them out. How is it supposed to look like?
'''
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
'''
print('Inventory:')
print(str(inv3.get('gold coin', 0)) + ' gold coins')
print(str(inv3.get('dagger', 0)) + ' dagger')
print(str(inv3.get('ruby', 0)) + ' ruby')
print(str(inv3.get('rope', 0)) + ' rope')
print("Total number of items: "+str(total))

# 4: Do total number of items. 

# 5: Do function.

# 6: Add previous project together.

