import sys
import dogUtil

potentialDrome = 'tacocat'

if len(sys.argv) == 1:
    print('Consider using the command line argument \'python3 ex6.py racecar\'')
    print('defaulting to "tacocat"')

if len(sys.argv) == 2:
        print('Received submission: ',sys.argv[1])
        potentialDrome = sys.argv[1]

dogUtil.palindromeCheck(potentialDrome)
