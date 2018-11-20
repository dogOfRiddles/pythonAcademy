import requests #incredibly powerful library.
import sys #this is how we'll manage command line parameters/arguments
import dogRandom
import random

howManyRandom = 1000
sysRandomList = []
howManySysRandom = 1000

if len(sys.argv) > 1:
    howManyRandom = sys.argv[1] #if someone wants to force the issue, let them set the number
    howManySysRandom = int(howManyRandom)

print('Collecting',howManySysRandom,'random values from Python\'s built in library')

while howManySysRandom != 0: #build our Python offering
    sysRandomList.append(random.randint(0,9))
    howManySysRandom = howManySysRandom -1

listOfRandoms = dogRandom.getRandomList(howManyRandom) #let the dogRandom take a shot
print('Collecting',howManyRandom,'numbers from random.org, generated from atmospheric noise.')

#print(refinedRandoms) #just to show our receipts, for debugging purposes

print('Harnessing this vast technology, let\'s see how many are over 5.') #HARNESS VAST SENSORS SIFTING SPACE FOR UTILITY

totalExceedingDogRandom = 0 #set an old school sentinel.

for index,element in enumerate(listOfRandoms): #enumerate was new to me here. index is a value that enumerate creates.
    if int(element) >= 5:
        #print('Value ',element,' found in element',index) #this is costly in screen real estate.
        totalExceedingDogRandom = totalExceedingDogRandom + 1
print('Total dogRandom element count above 5:',totalExceedingDogRandom) #show us the final count, SE style

totalExceedingPython = 0 #set an old school sentinel.

for index,element in enumerate(sysRandomList): #enumerate was new to me here. index is a value that enumerate creates.
    if int(element) >= 5:
        #print('Value ',element,' found in element',index) #this is costly in screen real estate.
        totalExceedingPython = totalExceedingPython + 1
print('Total Python element count above 5:',totalExceedingPython) #show us the final count, SE style
