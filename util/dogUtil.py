import dogRandom
import subprocess
import requests
import re
from pathlib import Path

def findLinksMore(textOfFile):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', textOfFile)
    return url

def md_scraper(fileToWork):
    mdHandler = open(fileToWork)
    urlList = []
    for line in mdHandler:
        urlsFound = findLinksMore(line)
        if len(urlsFound) != 0:
            urlList.append(re.sub('[\>\)\"\'\?\[\]\*]','',str(urlsFound)))

    print('\n**results of scraping',fileToWork+'**\n')

    for element in urlList:
        while element.find(',') != -1:
            urlStringLong = element.split(",")
            element = urlStringLong[0]

        while element.find(" ") != -1:
                urlStringLong = element.split(" ")
                element = urlStringLong[0]

        md_response = requests.get(str(element).strip())
        if md_response.status_code == 200:
            verboseResponse = '200 : OK'
        else:
            verboseResponse = str(md_response.status_code) + ' : Bad'
        print(element,verboseResponse)


def bubbleSort(unsortedList):
    n = len(unsortedList)
     # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if unsortedList[j] > unsortedList[j+1] :
                unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
    return unsortedList

def removeDuplicates(unsortedList):
    sortedList = []
    for index,element in enumerate(unsortedList):
        if element in sortedList:
            duplicate = True;
        else:
            sortedList.append(element)
    return sortedList


def fibonacci(requestedLength):
    if int(requestedLength < 2):
        requestedLength = 2
    depth = int(requestedLength) - 2 # to account for appends
    builtList = [1,1]
    marker = 0;
    while depth != marker:
        builtList.append((builtList[marker]+builtList[marker+1]))
        marker = marker + 1
    return builtList

def walkList(incomingList):
    for index,element in enumerate(incomingList):
        print(index,' : ',element)

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
