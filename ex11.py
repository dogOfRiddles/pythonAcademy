import dogUtil

import sys

argVariable = 10

if len(sys.argv) == 1:
    print('Consider using the command line argument \'python3 <script> <argument>\'')
    print('Defaulting to "default value"')

if len(sys.argv) == 2:
    print('Received submission: ',sys.argv[1])
    try:
        argVariable = int(sys.argv[1])
    except:
        print('Invalid Input. Reverting to default.')
        argVariable = 10

print('Providing the Fibonacci Sequence through element:',argVariable)

fibListForUser = dogUtil.fibonacci(argVariable)
dogUtil.walkList(fibListForUser)
