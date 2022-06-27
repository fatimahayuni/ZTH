essay = 'Marko, Kylo and Zaffo are three cute little baby bears who like to walk in the forest and meander around picking berries. Their mommy loves them very much'
count = {}

for character in essay:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
