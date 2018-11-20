import sys
import dogRandom

listLength = 12
evens = []

if len(sys.argv) == 1:
    print('Consider using the command line argument \'python3 ex7.py <listLength>\'')
    print('defaulting to "12"')

if len(sys.argv) == 2:
        print('Received submission: ',sys.argv[1])
        listLength = int(sys.argv[1])

randomList = dogRandom.getRandomList(listLength,0,100)

for index,element in enumerate(randomList):
    if int(element) % 2 == 0:
        evens.append(element)
        print(element,'found at index',index,'is submitted to new index:',len(evens)-1)
    else:
        print(element,'found at index',index,'is rejected for oddness.')
