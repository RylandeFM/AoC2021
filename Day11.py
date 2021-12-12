inputList, inputString = [], open("Input/Day 11.txt", "r").read().splitlines()

for line in inputString:
    inputList.append([int(x) for x in list(line)])

def solveBoth():
    octopusEnergy, totalFlashes, currentStep, hasFlashed = inputList[:], 0, 0, []
    while len(hasFlashed) < 100:
        currentStep += 1
        #increase global energy
        octopusEnergy = [[x+1 for x in line] for line in octopusEnergy]

        #handle all flashes
        hasFlashed = []
        flashes = getFlashing(octopusEnergy, hasFlashed)
        while len(flashes) > 0:
            for flash in flashes:
                hasFlashed.append(flash)
                for x in range(max(0, flash[0]-1),min(len(octopusEnergy), flash[0]+2)):
                    for y in range(max(0, flash[1]-1),min(len(octopusEnergy[0]), flash[1]+2)):
                        octopusEnergy[x][y] += 1
            flashes = getFlashing(octopusEnergy, hasFlashed)

        #set energy to 0 for flashed
        for coord in hasFlashed:
            octopusEnergy[coord[0]][coord[1]] = 0

        totalFlashes += len(hasFlashed)
        if currentStep == 100: print(totalFlashes)
    print(currentStep)

def getFlashing(board, hits):
    return [(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j]>9 and (i,j) not in hits]

solveBoth()
