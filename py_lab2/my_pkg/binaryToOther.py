def binaryToOct(binary):
    octNum = int(binary, 2)
    octNum = oct(octNum)
    octNum = octNum[2:]
    return octNum

def binaryToDec(binary):
    decNum = int(binary, 2)
    return decNum

def binaryToHex(binary):
    hexNum = int(binary, 2)
    hexNum = hex(hexNum)
    hexNum = hexNum[2:]
    hexNum = hexNum.upper()
    return hexNum
