import sys
import dogRandom
import dogUtil

argVariable = 0
listToBeTested = []
listOfChosenOnes = []

if len(sys.argv) == 1:
    print('Consider using the command line argument \'python3 <script> <argument>\'')
    #print('Defaulting to "default value"')

if len(sys.argv) == 2:
    print('Received submission: ',sys.argv[1])
    try:
        argVariable = 1
        listToBeTested = sys.argv[1].split(",")
    except:
        print('Invalid Input. Reverting to default.')
        argVariable = 0

if argVariable == 0:
    print('We\'ll collect a few values on our own.')
    listToBeTested = dogRandom.getRandomList(6)

print('Adding the first element to new list.')
listOfChosenOnes.append(listToBeTested[0])
print('Adding the last element to new list')
listOfChosenOnes.append(listToBeTested[len(listToBeTested)-1])

print('tested body of elements')
dogUtil.walkList(listToBeTested)

print('first and last elements')
dogUtil.walkList(listOfChosenOnes)
