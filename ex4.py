import requests
import sys # for the receiving of the command line arguments

if len(sys.argv) == 1:
    print('Consider using the command line argument \'python3 ex4.py <number>')
    print('Please submit a number. We will provide its perfect divisors.')
    try:
        numberToBeDivided = int(input())
    except:
        print('Your entry was not a number. Defaulting to 50.')
        numberToBeDivided = 50
else:
    try:
        numberToBeDivided = int(sys.argv[1])
    except:
        print('Your entry was not a number. Defaulting to 50.')
        numberToBeDivided = 50
        
print('We have received our number.')

divisors = range(1,numberToBeDivided)

for index,element in enumerate(divisors):
    if numberToBeDivided % element == 0:
        print(numberToBeDivided,'is divided by',element)
