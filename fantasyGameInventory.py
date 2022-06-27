print("Inventory:")
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
for k, v in stuff.items():
    print(str(v) + ' ' + k)

total = 0

for v in stuff.values():
    total += v

print("Total number of items: " + str(total))


