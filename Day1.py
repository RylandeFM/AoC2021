inputString = [int(x) for x in open("Input/Day 1.txt", "r").read().splitlines()]

def partOne():
    print(len([x for x in range(1,len(inputString)) if inputString[x]-inputString[x-1] > 0]))

def partTwo():
    print(len([x for x in range(1,len(inputString)-2) if inputString[x+2]-inputString[x-1] > 0]))

partOne()
partTwo()
