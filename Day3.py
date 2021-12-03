inputList = open("Input/Day 3.txt", "r").read().splitlines()

def solveBoth():
    g, e = "", ""

    for i in range(len(inputList[0])):
        s = sum([int(x[i]) for x in inputList]) 
        g += "0" if s < len(inputList)/2 else "1"
        e += "1" if s < len(inputList)/2 else "0"

    print(int(g,2)*int(e,2))
    print(int(findRating(inputList[:],"0","1"),2)*int(findRating(inputList[:],"1","0"),2))

def findRating(input, positive, negative):
    currentPos = 0
    while len(input) > 1:
        bit = positive if sum([int(x[currentPos]) for x in input]) < len(input)/2 else negative
        input = [x for x in input if x[currentPos]==bit]
        currentPos += 1
    return input[0]

solveBoth()
