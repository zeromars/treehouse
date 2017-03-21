#random.choice only works on things with indexes (not dictionaries)

#Create a function named nchoices() that takes an iterable and an integer. The function should return a list of n random items from the iterable where n is the integer. Duplicates are allowed.
import random
def nchoices(item,nums):
    answer = []
    x = 0
    while nums >= 1:
        rand = random.choice(item)
        answer.insert(x, rand)
        nums-=1
        x+=1
    return answer