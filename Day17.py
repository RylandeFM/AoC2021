bounds = [135, 155, -102, -78]

def partOne():
    print(sum(range(1,-bounds[2])))

def partTwo():
    validStarts = 0
    for originalX in range(lowestX(bounds[0]),bounds[1]+1):
        for originalY in range(bounds[2], -bounds[2]):
            x, y, xpos, ypos = originalX, originalY, 0, 0
            while ypos > bounds[2] and xpos < bounds[1]:
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