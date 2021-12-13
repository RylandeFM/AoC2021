inputString = open("Input/Day 13.txt", "r").read()

pointMap, folds = set(), []

for line in inputString.split("\n\n")[0].splitlines():
    x,y = line.split(",")
    pointMap.add((int(x),int(y)))

for line in inputString.split("\n\n")[1].splitlines():
    axis,place = line.split("along ")[1].split("=")
    folds.append((axis,int(place)))

def foldPoints():
    for e, fold in enumerate(folds):
        toFold = [point for point in pointMap if point[0 if fold[0]=="x" else 1] > fold[1]]
        for x, y in toFold:
            pointMap.remove((x, y))
            pointMap.add((x, fold[1]-(y-fold[1])) if fold[0]=="y" else (fold[1]-(x-fold[1]), y))
        if e == 0: print(len(pointMap))

def printMap():
    outputMap = [[" " for i in range(max([x for x,y in pointMap])+1)] for j in range(max([y for x,y in pointMap])+1)]
    for x, y in pointMap: outputMap[y][x] = "#"
    for line in outputMap: print("".join(line))
    
foldPoints()
printMap()