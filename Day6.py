from functools import cache

inputString = [int(i) for i in open("Input/Day 6.txt", "r").read().splitlines()[0].split(",")]

@cache
def reproduceFish(start, period, daysLeft):
    countOfFishes = 0

    if (daysLeft-start) < 0:
        return 0 #not enough days left to spawn more fish

    fishesSpawned = int((daysLeft-start)/period)+1
    for n in range(fishesSpawned):
        countOfFishes += reproduceFish(8, 7, daysLeft-start-(n*period)-1) #-1 because the spawn shows up next day

    return fishesSpawned + countOfFishes

def getAmountOfFish(days):
    ageSpawns = {}

    for age in set(inputString):
        ageSpawns[age] = reproduceFish(age, 7, days)+1

    print(sum([fish * inputString.count(age) for age, fish in ageSpawns.items()]))

getAmountOfFish(79)
getAmountOfFish(255)