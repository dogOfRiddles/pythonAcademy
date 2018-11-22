listOfWords = input("Submit a series of words: ").split()
reverseListOfWords = []

print(listOfWords)

for element in reversed(listOfWords): #reversing a list was cool
    reverseListOfWords.append(element)

print(reverseListOfWords)
