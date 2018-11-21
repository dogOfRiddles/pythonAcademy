import sys
import dogRandom
import random

argVariable = 0
randomNumber = int(dogRandom.getRandom()) % 10

if len(sys.argv) == 1:
    print('Consider using the command line argument \'python3 <script> <argument>\'')
    print('Defaulting to "default value"')

if len(sys.argv) == 2:
    print('Received submission: ',sys.argv[1])
    try:
        argVariable = sys.argv[1]
    except:
        print('Invalid Input. Reverting to default.')
        argVariable = 0
try:
    guess = int(input('Won\'t you make a guess at my number? Between 1 and 10.'))
except:
    print('That wasn\'t a number. Defaulting to a Python random')
    guess = random.randint(1,10)

print('You guessed',guess)

while guess != randomNumber:
    if guess > randomNumber:
        print('Too high.')
    if guess < randomNumber:
        print ('Too Low')
    if guess != randomNumber:
        try:
            guess = int(input('Guess again:'))
        except:
            guess = random.randint(1,10)
            print('That wasn\'t a number. Defaulting to a Python random')

if guess == randomNumber:
    print('You got it:',randomNumber)
    input('Press Enter to quit.')
