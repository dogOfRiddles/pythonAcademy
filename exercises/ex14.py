import requests
from bs4 import BeautifulSoup

fullText = requests.get('http://www.slashdot.org').text
fullSoup = BeautifulSoup(fullText,'html.parser')

for index,element in enumerate(fullSoup.find_all('a')):
    elementString = str(element.get('href'))
    if elementString.find('story') != -1:
        print(elementString)
