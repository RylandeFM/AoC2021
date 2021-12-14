inputString = open("Input/Day 14.txt", "r").read().splitlines()

operations = {}

for line in inputString[2:]:
        k, v = line.split(" -> ")
        operations[k] = v

def polymerize(steps):
    polyPairs, elements = {}, {}
    
    for i in range(2, len(inputString[0])+1):
        pair = inputString[0][i-2:i]
        polyPairs[pair] = 1 if pair not in polyPairs.keys() else polyPairs[pair] + 1

    for i in range(len(inputString[0])):
        elements[inputString[0][i]] = 1 if inputString[0][i] not in elements.keys() else elements[inputString[0][i]] + 1

    for _ in range(steps):
        newPairs = {}
        for pair, amount in polyPairs.items():
            elementAdded = operations[pair]

            elements[elementAdded] = amount if elementAdded not in elements.keys() else elements[elementAdded] + amount

            newPairs[pair[0]+elementAdded] = amount if pair[0]+elementAdded not in newPairs.keys() else newPairs[pair[0]+elementAdded] + amount
            newPairs[elementAdded+pair[1]] = amount if elementAdded+pair[1] not in newPairs.keys() else newPairs[elementAdded+pair[1]] + amount
        polyPairs = newPairs
    print(max(elements.values())-min(elements.values()))

polymerize(10)
polymerize(40)