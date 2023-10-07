import time
from random import randint
import random
def GenerateRandomNumbers():
    random_list = []
    howmany = int(input("How many numbers do you want to have in the list? "))
    for i in range(0, howmany):
        random_list.append(random.randint(0, 5000))
    return random_list

def linearSearch(myItem, myList):
    
    found = False
    position = 0
    
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position +1
    return found

returnedList = GenerateRandomNumbers()
print(returnedList)
userNumber = int(input("\nWhat number do you want to find: "))

theTime = str(time.perf_counter())
print("\nThe time before Linear searching ..... ", theTime)

isFound = linearSearch(userNumber, returnedList)

theTime = str(time.perf_counter())
print("\nThe time after Linear searching ..... ", theTime)

if isFound:
    print("\nThe number you typed is in the list...")
else:
    print("\nThe number you typed is not in the list...")