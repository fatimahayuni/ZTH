catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # this is the line of code that adds the number of cat input each time

    print('The cat names are:')
    for name in catNames:
        print('' + name)
