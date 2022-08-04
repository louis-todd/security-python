# Required imports
import hashlib

def avalancheCalculator(string1, string2):
    count = 0
    hash1 = getHash(string1)
    hash2 = getHash(string2)
    xor = int(hash1, 2) ^ int(hash2, 2)
    xor = bin(xor)
    for bit in xor:
        if(bit == "1"):
            count = count + 1
    return count

def getHash(string):
    hexValue = hashlib.sha256(string.encode()).hexdigest()
    binValue = bin(int(hexValue, 16))
    return binValue

string1 = "Hello World1"
string2 = "Hello World2"
print(avalancheCalculator(string1, string2))