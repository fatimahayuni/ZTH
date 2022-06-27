print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
elif feeling == 'not great':
    print("What's wrong?")
    whatswrong = input()
    if feeling == 'work':
        print('lots of calls huh?')
    else:
        print('Tomorrow will be a better day.')
