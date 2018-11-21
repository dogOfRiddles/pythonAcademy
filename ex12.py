import dogUtil
import dogRandom

print('We\'ll pull random numbers to be stripped of duplicates')
unsortedList = dogRandom.getRandomList(100,0,20)

dogUtil.walkList((dogUtil.removeDuplicates(unsortedList)))
