dragonLoot = {'gold coin': 3, 'dagger': 1, 'ruby': 1}
inv = {'gold coin': 42, 'rope': 1}

inv3 = {}

for d in dragonLoot, inv:
    for k, v in d.items():
        inv3[k] = inv3.get(k, 0) + v

print(inv3)
