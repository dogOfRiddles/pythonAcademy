import requests #incredibly powerful library.
import sys #this is how we'll manage command line parameters/arguments

howManyRandom = 1000

if len(sys.argv) > 1:
    howManyRandom = sys.argv[1] #if someone wants to force the issue, let them set the number

rawReturnedRandoms = requests.get('https://www.random.org/integers/?num='+str(howManyRandom)+'&min=0&max=9&col=1&base=10&format=plain&rnd=new')
rawReturnedQuota = requests.get('https://www.random.org/quota/?format=plain')
#print(rawReturnedRandoms.status_code) #check return code. 200 is OK
#print(rawReturnedRandoms.headers) #check the response header. There's a ton of info here.
print('Quota Remaining:',rawReturnedQuota.text.strip(),' - (uses about 6.5k per run)')

refinedRandoms = rawReturnedRandoms.text.replace("\n",",".strip())[:-1] #the [:-1] clips the last comma off of this replacement.

#define our list of elements
arrayOfRandoms = refinedRandoms.split(",")

print('Collecting',howManyRandom,'numbers from random.org, generated from atmospheric noise.')

#print(refinedRandoms) #just to show our receipts, for debugging purposes

print('Harnessing this vast technology, let\'s see how many are over 5.') #HARNESS VAST SENSORS SIFTING SPACE FOR UTILITY

totalExceeding = 0 #set an old school sentinel.

for index,element in enumerate(arrayOfRandoms): #enumerate was new to me here. index is a value that enumerate creates.
    if int(element) >= 5:
        #print('Value ',element,' found in element',index) #this is costly in screen real estate.
        totalExceeding = totalExceeding + 1
print('Total element count above 5:',totalExceeding) #show us the final count, SE style

#let's do some opining
#print(totalExceeding/int(howManyRandom))

if totalExceeding/int(howManyRandom) > .55 or totalExceeding/int(howManyRandom) < .45:
    print('That\'s some seriously unlikely randomisation, Square-Enix.')
