inputString = open("Input/Day 8.txt", "r").read().splitlines()

def partOne():
    print(sum([len([x for x in line.split(" | ")[1].split(" ") if len(x) in [2,3,4,7]]) for line in inputString]))

def partTwo():
    totalSum = 0

    for line in inputString:
        key, numbers = ["top","topLeft","topRight","middle","bottomLeft","bottomRight","bottom"], {}
        pattern, output = line.split(" | ")
        pattern, output = pattern.split(" "), output.split(" ")

        #numbers with length with one possibility
        numbers[1]=set([x for x in pattern if len(x) == 2][0])
        numbers[7]=set([x for x in pattern if len(x) == 3][0])
        numbers[4]=set([x for x in pattern if len(x) == 4][0])
        numbers[8]=set([x for x in pattern if len(x) == 7][0])
        key[0] = (numbers[7] - numbers[1])
        midAndTopLeft = numbers[4] - numbers[1]
        bottomAndBottomLeft = numbers[8] - numbers[4] - key[0]
        numbers[0] = set([x for x in pattern if len(x) == 6 and len(set(x)-key[0]-numbers[1]-bottomAndBottomLeft)==1][0])
        key[3] = (numbers[8] - numbers[0])
        key[1] = (midAndTopLeft - key[3])
        numbers[2] = set([x for x in pattern if len(x) == 5 and len(set(x)-key[0]-key[3]-bottomAndBottomLeft)==1][0])
        key[5] = (numbers[1]-numbers[2])
        key[2] = (numbers[1]-key[5])
        numbers[9] = set([x for x in pattern if len(x) == 6 and len(set(x)-key[0]-midAndTopLeft-numbers[1])==1][0])
        key[4] = (bottomAndBottomLeft-numbers[9])
        key[6] = (bottomAndBottomLeft-key[4])
        numbers[6] = set([x for x in pattern if len(set(x)-key[2]) == len(x) == 6][0])
        numbers[3] = set([x for x in pattern if len(set(x)-key[1]-key[4]) == len(x) == 5][0])
        numbers[5] = set([x for x in pattern if len(set(x)-key[2]-key[4]) == len(x) == 5][0])
    
        #apply code
        decodedOutput = [[number for number,pattern in numbers.items() if set(output[i])==pattern] for i in range(len(output))]
        totalSum += int("".join([str(x) for t in decodedOutput for x in t]))
    print(totalSum)

partOne()
partTwo()