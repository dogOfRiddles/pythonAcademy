import sys
import dogUtil

dogUtil.gatherSystemInfo()

if len(sys.argv) == 1 or len(sys.argv) == 2:
    print('Consider using the command line argument \'python3 <script> <argument> <argument>\'')
    print('Defaulting to "random"')
    dogUtil.adjudicateChops()

if len(sys.argv) == 3:
    print('Received submission: ',sys.argv[1],'and',sys.argv[2])
    try:
        player1 = sys.argv[1]
        player2 = sys.argv[2]
        dogUtil.adjudicateChops(player1,player2)
    except:
        print('Invalid Input. Reverting to default.')

#dogUtil.makeUserConfirm('heliotrope')
