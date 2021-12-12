from collections import defaultdict

inputString = open("Input/Day 12.txt", "r").read().splitlines()
caveMap, routes = defaultdict(list), set()

for line in inputString:
    left,right = line.split("-")
    caveMap[left] += [right]
    caveMap[right] += [left]

def findRoutes(currentNode, pathTravelled):
    if currentNode == "end":
        routes.add(tuple(pathTravelled))
        return

    for connection in caveMap[currentNode]:
        if connection.islower() and connection in pathTravelled: continue
        findRoutes(connection, pathTravelled + [connection])
    
    return(len(routes))

def findRoutesDoubleVisit(currentNode, pathTravelled):
    if currentNode == "end":
        routes.add(tuple(pathTravelled))
        return

    for connection in caveMap[currentNode]:
        if connection == "start" or connection.islower() and connection in pathTravelled and any(pathTravelled.count(visited) > 1 for visited in pathTravelled if visited.islower()): continue
        findRoutesDoubleVisit(connection, pathTravelled + [connection])
    
    return(len(routes))

print(findRoutes('start', ['start']))
print(findRoutesDoubleVisit('start', ['start']))