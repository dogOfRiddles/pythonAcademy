import sys
import dogUtil

argVariable = 0

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

dogUtil.makeUserConfirm('heliotrope')
