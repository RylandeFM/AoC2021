inputString = [int(x) for x in open("Input/Day 1.txt", "r").read().splitlines()]

def partOne():
    count = 0
    for index in range(1,len(inputString)):
        if inputString[index]-inputString[index-1] > 0: 
            count += 1
    print(count)

def partTwo():
    count = 0
    for index in range(1,len(inputString)-2):
        if (inputString[index]+inputString[index+1]+inputString[index+2])-(inputString[index-1]+inputString[index]+inputString[index+1]) > 0: 
            count += 1
    print(count)

partOne()
partTwo()
