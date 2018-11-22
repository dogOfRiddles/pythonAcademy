import requests
from bs4 import BeautifulSoup

fullText = requests.get('http://www.slashdot.org').text
fullSoup = BeautifulSoup(fullText,'html.parser')

# lots of text parsing to shave the links down to readable slashdot text
# element.get('href') will extract the content of any tag provided i.e 'href'

for index,element in enumerate(fullSoup.find_all('a')):
    elementString = str(element.get('href'))
    if elementString.find('story') != -1:
        if elementString.find('#comments') == -1:
            elementString = elementString[elementString.rfind('/')+1:len(elementString)]
            if elementString.find('?') != -1:
                elementString = elementString[0:elementString.find('?')]
            else:
                elementString = elementString

# learned a whole lot about find() here, and rfind() as well as the string[0,x] syntax

            if len(elementString) > 1:
                print(elementString.replace("-"," "))
