import requests

print('Exercise 2: The Way Things Are Different')

print('Could you consider submitting a number?')
whatTheUserDecides = input()
aDecidedNumber = int(whatTheUserDecides)

if (aDecidedNumber % 3) == 0:
    print('It\'s divisble by 3. How nice!')

if (aDecidedNumber % 4) == 0:
    print('It\'s divisible by 4. Nice digs.')

if (aDecidedNumber % 12) == 0:
    print('Wow, you\'re really testing this.')

if (aDecidedNumber % 88) == 0:
    print('Q is among us!')
    trumpURL = 'https://api.whatdoestrumpthink.com/api/v1/quotes/random'
    r = (requests.get(trumpURL).json())
    print(r['message'])
# may his message be mocked for all days
