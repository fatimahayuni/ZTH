favoriteColors = {'Ayuni': 'Blue', 'Matt': 'Green', 'Karl': 'Yellow'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()

    if name in favoriteColors:
        print(favoriteColors[name] + ' is the favorite color of ' + name)
    else:
        print('I do not have favorite color information for ' + name)
        print('What is their favorite color?')
        favColor = input()
        favoriteColors[name] = favColor
        print('Favorite colors database updated.')

    if name == '':
        break
