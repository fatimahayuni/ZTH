dragonLoot = {'gold coin': 3, 'dagger': 1, 'ruby': 1}
inv = inv = {'gold coin': 42, 'rope': 1}

dict_2 = {'Bonnie': 18, 'Rick': 20, 'Matt': 16}

def mergeDictionary(dragonLoot, inv):
   dict_3 = {**dragonLoot, **inv}
   for key, value in dict_3.items():
       if key in dragonLoot and key in inv:
               dict_3[key] = [value , dragonLoot[key]]
   return dict_3

dict_3 = mergeDictionary(dragonLoot, inv)
print(dict_3)
