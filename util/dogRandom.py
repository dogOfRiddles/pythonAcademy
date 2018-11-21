import requests

def getRandomListOld(howManyRandom): #deprecated
    rawReturnedRandoms = requests.get('https://www.random.org/integers/?num='+str(howManyRandom)+'&min=0&max=9&col=1&base=10&format=plain&rnd=new')
    rawReturnedQuota = requests.get('https://www.random.org/quota/?format=plain')

    #print(rawReturnedRandoms.status_code) #check return code. 200 is OK
    #print(rawReturnedRandoms.headers) #check the response header. There's a ton of info here.
    print('Quota Remaining:',rawReturnedQuota.text.strip())

    refinedRandoms = rawReturnedRandoms.text.replace("\n",",".strip())[:-1] #the [:-1] clips the last comma off of this replacement.
    return refinedRandoms.split(",")

def getRandomList(howManyRandom,minNumber = -1 ,maxNumber = -1):
    if minNumber == -1 or maxNumber == -1:
        rawReturnedRandoms = requests.get('https://www.random.org/integers/?num='+str(howManyRandom)+'&min=0&max=9&col=1&base=10&format=plain&rnd=new')
        rawReturnedQuota = requests.get('https://www.random.org/quota/?format=plain')

        #print(rawReturnedRandoms.status_code) #check return code. 200 is OK
        #print(rawReturnedRandoms.headers) #check the response header. There's a ton of info here.
        print('Quota Remaining:',rawReturnedQuota.text.strip())

        refinedRandoms = rawReturnedRandoms.text.replace("\n",",".strip())[:-1] #the [:-1] clips the last comma off of this replacement.
        return refinedRandoms.split(",")
    else:
        rawReturnedRandoms = requests.get('https://www.random.org/integers/?num='+str(howManyRandom)+'&min='+str(minNumber)+'&max='+str(maxNumber)+'&col=1&base=10&format=plain&rnd=new')
        rawReturnedQuota = requests.get('https://www.random.org/quota/?format=plain')

        #print(rawReturnedRandoms.status_code) #check return code. 200 is OK
        #print(rawReturnedRandoms.headers) #check the response header. There's a ton of info here.
        print('Quota Remaining:',rawReturnedQuota.text.strip())

        refinedRandoms = rawReturnedRandoms.text.replace("\n",",".strip())[:-1] #the [:-1] clips the last comma off of this replacement.
        return refinedRandoms.split(",")

def getRandomString(howManyRandom):
    rawReturnedRandoms = requests.get('https://www.random.org/integers/?num='+str(howManyRandom)+'&min=0&max=9&col=1&base=10&format=plain&rnd=new')
    rawReturnedQuota = requests.get('https://www.random.org/quota/?format=plain')

    #print(rawReturnedRandoms.status_code) #check return code. 200 is OK
    #print(rawReturnedRandoms.headers) #check the response header. There's a ton of info here.
    print('Quota Remaining:',rawReturnedQuota.text.strip(),' - (uses about 6.5k per run)')

    refinedRandoms = rawReturnedRandoms.text.replace("\n",",".strip())[:-1] #the [:-1] clips the last comma off of this replacement.

def getRandom():
    rawReturnedRandoms = requests.get('https://www.random.org/integers/?num=1&min=0&max=1000&col=1&base=10&format=plain&rnd=new')
    rawReturnedQuota = requests.get('https://www.random.org/quota/?format=plain')
    print('Quota Remaining:',rawReturnedQuota.text.strip())
    return rawReturnedRandoms.text #the [:-1] clips the last comma off of this replacement.
