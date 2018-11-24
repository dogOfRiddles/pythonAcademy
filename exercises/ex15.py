import random

randomNumber = random.randint(1000, 9999)
randomNumberList = []
for element in str(randomNumber):
    randomNumberList.append(element)

guess = '0000'
cow = 0
bull = 0

while guess != randomNumber:

    guessList = []
    cow = 0
    bull = 0

    for index, element in enumerate(str(guess)):
        guessList.append(element)
        if element in randomNumberList:
            if element == randomNumberList[index]:
                bull = bull + 1
                guessList[index] = '*'
            else:
                cow = cow + 1
    print(guessList)
    print('cows: ', cow, 'bulls: ', bull)

    if guess != randomNumber:
        try:
            guess = input('Guess again (q to exit):')
            if str(guess) == 'q':
                print('The random number was:', randomNumber)
                exit(0)
            guess = int(guess)
        except:
            print(guess)
            if str(guess) == 'q':
                exit()
            guess = random.randint(1000, 9999)
            print('That wasn\'t a number. Defaulting to a Python random:', guess)

print('The random number was: ', guess)
