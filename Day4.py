inputString = open("Input/Day 4.txt", "r").read().splitlines()

numbers = [int(x) for x in inputString[0].split(",")]
boards, board = [], []
for line in inputString[2:]:
    if line == "":
        boards.append(board)
        board = []
    else:
        board.append([int(x) for x in line.strip().replace("  ", " ").split(" ")])

def solveBoth():
    currentCalled = numbers[:4]
    maxLength = len(boards)
    for number in numbers[4:]:
        currentCalled.append(number)
        for board in boards:
            if checkBoard(currentCalled, board):
                if len(boards) == maxLength: #first board to score is the solution to the first part
                    print(sum([x for x in [item for subList in board for item in subList] if x not in currentCalled])*number)
                    boards.remove(board)
                elif len(boards) == 1: #last board to score is the solution to the last part, can stop after
                    print(sum([x for x in [item for subList in board for item in subList] if x not in currentCalled])*number)
                    return
                else:
                    boards.remove(board)

def checkBoard(calledNumbers, board):
    for i in range(len(board[0])):
        if len([x for x in board[i] if x not in calledNumbers]) == 0:
            return True
        if len([x for x in list(zip(*board))[i] if x not in calledNumbers]) == 0:
            return True
    return False

solveBoth()
