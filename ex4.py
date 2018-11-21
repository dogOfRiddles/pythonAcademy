import sys # for the receiving of the command line arguments
import dogRandom

notPrime = False

if len(sys.argv) == 1:
    print('Consider using the command line argument \'python3 ex4.py <number>')
    print('Please submit a number. We will provide its perfect divisors.')

    try: #Because it's user input, we have to check it a bit.
        numberToBeDivided = int(input())
    except:
        print('Your entry was not a number. Defaulting to a random number.')
        numberToBeDivided = int(dogRandom.getRandom())
else:
    try: #the command line argument is user input, too. Check it.
        numberToBeDivided = int(sys.argv[1])
    except:
        print('Your entry was not a number. Defaulting to a random number.')
        numberToBeDivided = int(dogRandom.getRandom())

print('Perfect divisors for ',numberToBeDivided,':')

divisors = range(1,numberToBeDivided) #the range() method returns the range of numbers between parameters

for index,element in enumerate(divisors): #here's enumerate() again. Just in case we needed its index.
    if numberToBeDivided % element == 0:
        print(numberToBeDivided,'is divided by',element)
        notPrime = True

if notPrime: #this is for ex12
    print('**Prime Number**')
