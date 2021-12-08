inputString = open("Input/Day 8.txt", "r").read().splitlines()

def partOne():
    count = 0
    for line in inputString:
        for outputSignal in line.split(" | ")[1].split(" "):
            if len(outputSignal) in [2,3,4,7]: count += 1
    print(count)

def partTwo():
    totalSum = 0

    for line in inputString:
        key = ["","","","","","",""]
        pattern, output = line.split(" | ")
        numbers = {}
        pattern = pattern.split(" ")
        output = output.split(" ")

        #numbers with length with one possibility
        numbers[1]=set([x for x in pattern if len(x) == 2][0])
        numbers[7]=set([x for x in pattern if len(x) == 3][0])
        numbers[4]=set([x for x in pattern if len(x) == 4][0])
        numbers[8]=set([x for x in pattern if len(x) == 7][0])
        right = numbers[1]
        top = numbers[7] - numbers[1]
        midAndTopLeft = numbers[4] - numbers[1]
        bottomAndBottomLeft = numbers[8] - numbers[4] - top
        key[0] = top.pop()
        zero = [x for x in pattern if len(x) == 6 and len(set(x)-set(key[0])-numbers[1]-bottomAndBottomLeft)==1] #0
        numbers[0] = set(zero[0])
        middle = numbers[8] - numbers[0]
        key[3] = middle.pop()
        key[1] = (midAndTopLeft - set(key[3])).pop()
        two = [x for x in pattern if len(x) == 5 and len(set(x)-set(key[0])-set(key[3])-bottomAndBottomLeft)==1]
        numbers[2] = set(two[0])
        key[5] = (numbers[1]-set(two[0])).pop()
        key[2] = (numbers[1]-set(key[5])).pop()
        nine = [x for x in pattern if len(x) == 6 and len(set(x)-set(key[0])-midAndTopLeft-numbers[1])==1]
        numbers[9] = set(nine[0])
        key[4] = (bottomAndBottomLeft-set(nine[0])).pop()
        key[6] = (bottomAndBottomLeft-set(key[4])).pop()
        numbers[6] = set([x for x in pattern if key[2] not in x and len(x) == 6][0])
        numbers[3] = set([x for x in pattern if key[1] not in x and key[4] not in x and len(x) == 5][0])
        numbers[5] = set([x for x in pattern if key[2] not in x and key[4] not in x and len(x) == 5][0])
    
        #apply code
        decodedOutput = [[number for number,pattern in numbers.items() if set(output[i])==pattern] for i in range(len(output))]
        totalSum += int("".join([str(x) for t in decodedOutput for x in t]))
    print(totalSum)

partOne()
partTwo()