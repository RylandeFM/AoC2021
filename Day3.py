inputString = open("Input/Day 3.txt", "r").read().splitlines()

def solveBoth():
    diagList, g, e = [], "", ""
    for line in inputString:
        diagList.append(line)

    for i in range(len(diagList[0])):
        s = sum([int(x[i]) for x in diagList]) 
        g += "0" if s < len(diagList)/2 else "1"
        e += "1" if s < len(diagList)/2 else "0"

    print(int(g,2)*int(e,2))
    print(int(findRating(diagList[:],"0","1"),2)*int(findRating(diagList[:],"1","0"),2))

def findRating(diagList, positive, negative):
    currentPos = 0
    while len(diagList) > 1:
        bit = positive if sum([int(x[currentPos]) for x in diagList]) < len(diagList)/2 else negative
        diagList = [x for x in diagList if x[currentPos]==bit]
        currentPos += 1
    return diagList[0]

solveBoth()
