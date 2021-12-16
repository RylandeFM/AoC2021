from functools import reduce

inputString = open("Input/Day 16.txt", "r").read()

def parsePacket(packet, values):
    version, type, packet = int(packet[:3], 2), int(packet[3:6], 2), packet[6:]
    versions.append(version)
    if type == 4:
        literal = ""
        while packet[0] != "0": 
            literal += packet[1:5]
            packet = packet[5:]
        literal += packet[1:5]
        values.append(int(literal, 2))
        return packet[5:], values
    if packet[0] == "0":
        length, packet = int(packet[1:16], 2), packet[16:]
        subPacket, packet = packet[:length], packet[length:]
        while len(subPacket) != 0 and int(subPacket, 2) > 0: 
            subPacket, subValue = parsePacket(subPacket, [])
            values += subValue
    else:
        subPackets, packet = int(packet[1:12], 2), packet[12:]
        for _ in range(subPackets): 
            packet, subValue = parsePacket(packet, [])
            values += subValue

    if type == 0: return packet, [sum(values)]
    if type == 1: return packet, [reduce((lambda x, y: x * y), values)]
    if type == 2: return packet, [min(values)]
    if type == 3: return packet, [max(values)]
    if type == 5: return packet, [1 if values[0] > values[1] else 0]
    if type == 6: return packet, [1 if values[0] < values[1] else 0]
    if type == 7: return packet, [1 if values[0] == values[1] else 0]

versions, values = [], []
_, values = parsePacket(bin(int(inputString, 16))[2:].zfill(len(inputString) * 4), [])
print(sum(versions))
print(values[0])