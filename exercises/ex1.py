from datetime import datetime  # without it, we are lost
from datetime import timedelta  # something must change

theDaySheBegan = datetime.strptime('9 Nov 1984', '%d %b %Y')

# and yet, we must make the attempt. The Request.
print('Exercise 1 - Wherein we speak of a time that may never come\n')
print('Enter a date of birth, please. In the nature of \'10-06-1983\', perhaps')

# here is where our trust is laid down. Here, we could come to ruin.
userProbablyNotRealBirthday = input()
# it could be anything, but the damage is done now.

print('You entered:', userProbablyNotRealBirthday, 'which we hope is a date of birth.')
# may there be many days like it

try:
    whereDatesGoToDie = datetime.strptime(userProbablyNotRealBirthday, '%m-%d-%Y')
    # this, the test. If we have done our part well? There is power in this moment.
except:
    print('It was not a date. We have lost ourselves in the fray.')
    whereDatesGoToDie = ''
    # it had to come eventually
else:
    theSunlitDaySomeday = whereDatesGoToDie + timedelta(36500)
    # may it pass us as a friend, and go on when the time comes
    print('So be it.\n**************')
    # may the day come with something bright and fierce
    print('In one hundred years, your birthday will fall on a', theSunlitDaySomeday.strftime('%A'),'in the year',theSunlitDaySomeday.year)
    # may the year see wonders and unknown trials. May someone remember you.
if whereDatesGoToDie == theDaySheBegan:
    # may they have bliss
    print('Peegs Everyday Forever `(^oo^)`')
