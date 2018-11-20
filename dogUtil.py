import dogRandom
import subprocess

def gatherSystemInfo():
    p1 = subprocess.Popen(['uptime'], stdout=subprocess.PIPE)
    # Run the command
    output = p1.communicate()[0]
    print(output[:-1])

def palindromeCheck(potentialDrome):
    dromeLength = len(potentialDrome)
    dromeTruth = False
    for index,element in enumerate(potentialDrome):
        print(potentialDrome[index],'equals',potentialDrome[dromeLength-1-index])
        if (potentialDrome[index] == potentialDrome[dromeLength-1-index]):
            dromeTruth = True
        else:
            dromeTruth = False
    if dromeTruth:
        print('It\'s a palindrome, y\'all!')

def makeUserConfirm(confirmString):
    quit = input('Type "'+confirmString+'" to confirm your choice:' )
    while quit != confirmString:
        quit = input('Type "'+confirmString+'" to confirm your choice:' )

def adjudicateChops(player1 = 'none' ,player2 = 'none'):
    if player2 == 'none' and player1 == 'none':
        player1 = int(dogRandom.getRandom()) % 3
        player2 = int(dogRandom.getRandom()) % 3

    if player2 == 'none' and player1 != 'none':
        player2 = int(dogRandom.getRandom()) % 3

    print(player1,'-',player2)

    player1 = int(player1)
    player2 = int(player2)

    if player1 == 0 and player2 == 1:
        print('Player 2 wins with Paper!')
    if player1 == 0 and player1 == 2:
        print('Player 1 wins with Rock!')
    if player1 == 2 and player2 == 0:
        print('Player 2 wins with Rock!')
    if player1 == 1 and player2 == 0:
        print('Player 1 wins with Paper!')
    if player1 == 1 and player2 == 2:
        print('Player 2 wins with Scissors!')
    if player1 == 2 and player2 == 1:
        print('Player 1 wins with Scissors!')
    if player1 == player2:
        print('A tie!')
