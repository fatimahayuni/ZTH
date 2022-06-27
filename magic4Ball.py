import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    if answerNumber == 2:
        return 'It is decidedly so'
    if answerNumber == 3:
        return 'Yes'
    if answerNumber == 4:
        return 'Reply hazy try again'

print(getAnswer(random.randint(1,4)))
