import sys
import dogRandom

if len(sys.argv) == 1 or len(sys.argv) == 2:
    print('Consider using the command line argument \'python3 ex5.py <listLength1> <listLength2>')
    print('Creating two random lists, lengths 10 and 12.')
    listLength1 = 10
    listLength2 = 12

if len(sys.argv) == 3:
    try: #Because it's user input, we have to check it a bit.
        listLength1 = int(sys.argv[1])
        listLength2 = int(sys.argv[2])
    except:
        print('Your entry was not a number. Defaulting to a random number.')
        listLength1 = 10
        listLength2 = 12

randomListA = dogRandom.getRandomList(listLength1,0,50) #using new overloaded method
randomListB = dogRandom.getRandomList(listLength2,0,50) #using new overloaded method

for index,element in enumerate(randomListA):
    if element in randomListB:
        print('Found Mutually Between Lists: ',element)
