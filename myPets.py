'''
Enter a pet name:
'''

cats = ['Milo', 'Quantro', 'Spaghetti', 'Burrata', 'Twofoot']
print('Enter a pet name:')
name = input()
if name not in cats:
    print('We cannot find a cat named ' + name + '. Do you want to find another cat? Type Y for yes. Type N for no.')
    answer = input()
    if answer == 'Y':
        print('Enter a pet name:')
        name = input()
else:
    print('We found a cat named ' + name + '.')
   
