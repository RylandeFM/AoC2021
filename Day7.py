inputString = [int(i) for i in open("Input/Day 7.txt", "r").read().splitlines()[0].split(",")]
#inputString = [16,1,2,0,4,2,7,1,2,14]

def partOne():
    minFuel = 9999999999999999
    for i in range(min(inputString), max(inputString)+1):
        sumOfFuel = sum([abs(i - x) for x in inputString])
        if sumOfFuel < minFuel:
            minFuel = sumOfFuel
            minI = i
    print(minI, minFuel)

def partTwo():
    minFuel = 9999999999999999
    for i in range(min(inputString), max(inputString)+1):
        sumOfFuel = sum([sum(range(abs(i - x)+1)) for x in inputString])
        if sumOfFuel < minFuel:
            minFuel = sumOfFuel
            minI = i
    print(minI, minFuel)

partOne()
partTwo()