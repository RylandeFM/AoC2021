import heapq

inputString = open("Input/Day 15.txt", "r").read().splitlines()
grid = [[int(x) for x in line] for line in inputString]

def findRoute(start, end):
    visited, queue = {}, [start]
    heapq.heapify(queue)

    while len(queue) > 0:
        x, y = heapq.heappop(queue)
        risk = visited.get((x,y), 0)
        for a,b in getNeighbours((x,y), end):
            newRisk = risk + grid[a][b]
            if (a,b) not in visited.keys() or visited[(a, b)] > newRisk:
                visited[(a, b)] = newRisk
                heapq.heappush(queue, (a, b))
    print(visited[end])

def getNeighbours(point, end):
    x, y = point
    for a, b in (0, 1), (1, 0), (0, -1), (-1, 0):
        if 0 <= (x + a) <= end[0] and 0 <= (y + b) <= end[1]:
            yield (x + a, y + b)

def increaseGrid(oldGrid):
    newGrid = []
    for i in range(5):
        for line in oldGrid:
            newLine = []
            for j in range(5):
                newLine += [((i + j + n - 1) % 9) + 1 for n in line]
            newGrid.append(newLine)
    return newGrid


findRoute((0,0), (len(grid)-1, len(grid[0])-1))
grid = increaseGrid(grid)
findRoute((0,0), (len(grid)-1, len(grid[0])-1))