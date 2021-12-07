inputString = [int(i) for i in open("Input/Day 7.txt", "r").read().splitlines()[0].split(",")]

def partOne():
    print(min(sum(abs(i - x) for x in inputString) for i in range(min(inputString), max(inputString) + 1)))

def partTwo():
    print(min(sum(int(abs(i - x)*((abs(i - x)+1)/2)) for x in inputString) for i in range(min(inputString), max(inputString) + 1)))

partOne()
partTwo()