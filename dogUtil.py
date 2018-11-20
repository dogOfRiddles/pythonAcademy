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
