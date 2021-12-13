inputString = open("Input/Day 13.txt", "r").read()

pointMap, folds = set(), []

for line in inputString.split("\n\n")[0].splitlines():
    x,y = line.split(",")
    pointMap.add((int(x),int(y)))

for line in inputString.split("\n\n")[1].splitlines():
    axis,place = line.split("along ")[1].split("=")
    folds.append((axis,int(place)))

def foldPoints():
    global pointMap
    firstFold = True
    for axis, place in folds:
        newMap = set()
        if axis == "y":
            for x, y in pointMap:
                if y < place:
                    newMap.add((x, y))
                else:
                    newMap.add((x, place-(y-place)))
        else:
            for x, y in pointMap:
                if x < place:
                    newMap.add((x, y))
                else:
                    newMap.add((place-(x-place), y))
        if firstFold:
            print(len(newMap))
            firstFold = False
        pointMap = newMap

def printMap():
    outputMap = [[" " for i in range(max([x for x,y in pointMap])+1)] for j in range(max([y for x,y in pointMap])+1)]
    for x, y in pointMap: outputMap[y][x] = "#"
    for line in outputMap: print("".join(line))
    
foldPoints()
printMap()