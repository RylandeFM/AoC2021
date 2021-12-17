#inputString = open("Input/Day 17.txt", "r").read().splitlines()
bounds = [135, 155, -102, -78]

def partOne():
    highestPoint, targetY = 0, [y for y in range(bounds[2], bounds[3]+1)]
    for y in range(lowestX(bounds[0]), -bounds[2]+1):
        originalY, yPos = y, 0
        while yPos not in targetY and yPos > bounds[3]:
            yPos += y
            y -= 1
        if yPos in targetY: highestPoint = max(highestPoint, sum(range(1,originalY+1)))
    print(highestPoint)

def partTwo():
    validStarts = 0
    for originalX in range(lowestX(bounds[0]),bounds[1]+1):
        for originalY in range(bounds[2], -bounds[2]):
            x, y, xpos, ypos = originalX, originalY, 0, 0
            while x > 0 or ypos > bounds[2]:
                xpos, ypos = xpos + x, ypos + y
                x, y = max(0, x - 1), y - 1
                if bounds[0] <= xpos <= bounds[1] and bounds[2] <= ypos <= bounds[3]:
                    validStarts += 1
                    break
    print(validStarts)

def lowestX(target):
    sum, i = 0, 1
    while sum < target: sum, i = sum + i, i + 1
    return i - 1

partOne()
partTwo()
