names = ['Anna', 'Faizal', 'Fylvia', 'Karl', 'Maria', 'Matt']
print('\n'.join(names))

newname = input('Enter a new name: ')
names.append(newname)
names.sort()
print('\n'.join(names))
