import json
inputList = open("Input/Day 18.txt", "r").read().splitlines()

def doHomework(inputList):
    currentSnailNumber = ""
    for s in inputList:
        currentSnailNumber = reduceSnailNumber("[" + currentSnailNumber + "," + s + "]") if currentSnailNumber != "" else s

    return magnitudeSnailNumber(json.loads(currentSnailNumber))

def reduceSnailNumber(snailNumber):
    snailList = json.loads(snailNumber)
    depth, highest = getDepth(snailList), getMaximum(snailList)

    while depth > 4 or highest > 9:
        snailNumber = explodeSnailNumber(snailNumber) if depth > 4 else splitSnailNumber(snailNumber)
        snailList = json.loads(snailNumber)
        depth, highest = getDepth(snailList), getMaximum(snailList)

    return snailNumber
    
def explodeSnailNumber(snailNumber):
    count, start, end = 0, 0, 0

    for i, c in enumerate(snailNumber):
        if c == '[': count += 1
        
        if count == 5:
            start, end = i, i
            while not snailNumber[start+1].isnumeric() or not snailNumber[start+3].isnumeric():
                start += 1
            if snailNumber[start].isnumeric(): start -= 1
            while not snailNumber[end] == ']':
                end += 1
            break
        
        if c == ']': count -= 1

    leftNumber, rightNumber = snailNumber[start+1:end].split(",")
    left, right = snailNumber[:start], snailNumber[end+1:]

    for i in range(len(left)-1, 0, -1):
        if left[i].isnumeric():
            if left[i-1].isnumeric():
                left = left[:i-1] + str(int(left[i-1:i+1]) + int(leftNumber)) + left[i+1:]
            else:
                left = left[:i] + str(int(left[i]) + int(leftNumber)) + left[i+1:]
            break

    for i in range(len(right)):
        if right[i].isnumeric():
            if right[i+1].isnumeric():
                right = right[:i] + str(int(right[i:i + 2]) + int(rightNumber)) + right[i + 2:]
            else:
                right = right[:i] + str(int(right[i:i + 1]) + int(rightNumber)) + right[i + 1:]
            break

    return left + "0" + right

def splitSnailNumber(snailNumber):
    for i in range(len(snailNumber)):
        if snailNumber[i].isnumeric() and snailNumber[i+1].isnumeric():
            left, right, number = snailNumber[:i], snailNumber[i + 2:], int(snailNumber[i:i+2])
            break

    return left + "[" + str(number // 2) + "," + str(number // 2 + (number % 2)) + "]" + right

def getDepth(snailList, count = 0):
    return count if not isinstance(snailList,list) else max([getDepth(x,count+1) for x in snailList])

def getMaximum(snailList):
    return snailList if not isinstance(snailList,list) else max([getMaximum(x) for x in snailList])

def magnitudeSnailNumber(snailNumber):
    return 3 * (snailNumber[0] if isinstance(snailNumber[0],int) else magnitudeSnailNumber(snailNumber[0])) + 2 * (snailNumber[1] if isinstance(snailNumber[1],int) else magnitudeSnailNumber(snailNumber[1]))

print(doHomework(inputList))
print(max([doHomework([inputList[i],inputList[j]]) for i in range(len(inputList)) for j in range(len(inputList)) if i != j]))
