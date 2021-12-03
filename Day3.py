inputString = open("Input/Day 3.txt", "r").read().splitlines()

def solveBoth():
    binList, g, e = [], "", ""
    for line in inputString:
        binList.append(line)

    for i in range(len(binList[0])):
        s = sum([int(x[i]) for x in binList]) 
        g += "0" if s < len(binList)/2 else "1"
        e += "1" if s < len(binList)/2 else "0"

    print(int(g,2)*int(e,2))
    print(int(findRating(binList[:],"0","1")[0],2)*int(findRating(binList[:],"1","0")[0],2))

def findRating(binList, positive, negative):
    currentPos = 0
    while len(binList) > 1:
        bit = positive if sum([int(x[currentPos]) for x in binList]) < len(binList)/2 else negative
        binList = [x for x in binList if x[currentPos]==bit]
        currentPos += 1
    return binList

solveBoth()
