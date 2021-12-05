inputString = open("Input/Day 5.txt", "r").read().splitlines()

def partOne():
    points = {}
    for line in inputString:
        x, y =[None,None], [None,None]
        x[0],y[0],x[1],y[1] = [int(i) for i in line.replace(' -> ', ',').split(',')]
        if x[0] == x[1] or y[0] == y[1]:
            for a in range(min(x), max(x)+1):
                for b in range(min(y), max(y)+1):
                    points[(a,b)] = 1 if (a,b) not in points.keys() else points[(a,b)]+1
    print(len([x for x in points.values() if x > 1]))
    return points

def partTwo(points):
    for line in inputString:
        x, y =[None,None], [None,None]
        x[0],y[0],x[1],y[1] = [int(i) for i in line.replace(' -> ', ',').split(',')]
        if x[0] != x[1] and y[0] != y[1]:
            stepX = 1 if x[0] < x[1] else -1
            stepY = 1 if y[0] < y[1] else -1
            for a,b in list(zip(range(x[0],x[1]+stepX,stepX),range(y[0],y[1]+stepY,stepY))):
                points[(a,b)] = 1 if (a,b) not in points.keys() else points[(a,b)]+1
    print(len([x for x in points.values() if x > 1]))

partTwo(partOne())