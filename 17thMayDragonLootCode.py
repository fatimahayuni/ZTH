dragonLoot = {'gold coin': 3, 'dagger': 1, 'ruby': 1}
inv  = {'gold coin': 42, 'rope': 1}
newDictionary= dragonLoot = inv


print(str(dragonLoot.get('gold coin', 0)))
