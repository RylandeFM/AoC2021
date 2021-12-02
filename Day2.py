inputString = open("Input/Day 2.txt", "r").read().splitlines()

def partOne():
    [hor, dep] = [0, 0]
    for line in inputString:
        [com, amt] = line.split(" ")
        if (com == "forward"):
            hor += int(amt)
        elif (com == "down"):
            dep += int(amt)
        elif (com == "up"):
            dep -= int(amt)
        else:
            print("Error")
    print(hor * dep)

def partTwo():
    [hor, dep, aim] = [0, 0, 0]
    for line in inputString:
        [com, amt] = line.split(" ")
        if (com == "forward"):
            hor += int(amt)
            dep += int(amt) * aim
        elif (com == "down"):
            aim += int(amt)
        elif (com == "up"):
            aim -= int(amt)
        else:
            print("Error")
    print(hor * dep)

partOne()
partTwo()