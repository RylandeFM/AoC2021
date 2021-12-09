inputString = open("Input/Day 9.txt", "r").read().splitlines()
inputList = []

for line in inputString:
    inputList.append([int(x) for x in list(line)])

def partOne():
    lowestPoints, sumLowest = [], 0
    for i, line in enumerate(inputList):
        for j, height in enumerate(line):
            if j > 0 and line[j-1]<=height: continue
            if j < len(line)-1 and line[j+1]<=height: continue
            if i > 0 and inputList[i-1][j]<=height: continue
            if i < len(inputList)-1 and inputList[i+1][j]<=height: continue
            sumLowest += height+1
            lowestPoints.append((i, j))
    print(sumLowest)
    return lowestPoints

def partTwo(lowestPoints):
    basinSizeList = []
    for lowPoint in lowestPoints:
        pointReviewSet, checkedPoints = set(), []
        pointReviewSet.add(lowPoint)
        while len(pointReviewSet) > 0:
            p = pointReviewSet.pop()
            checkedPoints.append(p)
            if p[0] > 0 and (p[0]-1, p[1]) not in checkedPoints and inputList[p[0]-1][p[1]] < 9: pointReviewSet.add((p[0]-1, p[1]))
            if p[0] < len(inputList)-1 and (p[0]+1, p[1]) not in checkedPoints and inputList[p[0]+1][p[1]] < 9: pointReviewSet.add((p[0]+1, p[1]))
            if p[1] > 0 and (p[0], p[1]-1) not in checkedPoints and inputList[p[0]][p[1]-1] < 9: pointReviewSet.add((p[0], p[1]-1))
            if p[1] < len(inputList[0])-1 and (p[0], p[1]+1) not in checkedPoints and inputList[p[0]][p[1]+1] < 9: pointReviewSet.add((p[0], p[1]+1))
        basinSizeList.append(len(checkedPoints))
    basinSizeList.sort(reverse=True)
    print(basinSizeList[0]*basinSizeList[1]*basinSizeList[2])

partTwo(partOne())