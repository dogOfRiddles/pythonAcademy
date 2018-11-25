import sys

argVariable = 0

if len(sys.argv) == 1:
    print('FYI: command line argument \'python3 <script> <argument>\'')
    print('Defaulting to "default value"')

if len(sys.argv) == 2:
    print('Received submission: ', sys.argv[1])
    try:
        argVariable = sys.argv[1]
    except Exception:
        print('Invalid Input. Reverting to default.')
        argVariable = 0
