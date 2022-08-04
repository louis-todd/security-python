# Required imports
import string

alphabet = {}

def createAlphabet():
    #adding all uppercase ascii to alphabet
    for i in range (65, 91):
        alphabet.update({i % 26: chr(i)})


def encryptAffine(plainText, a, b):
    createAlphabet()
    #creating blank cipher text string
    cipherText = ""
    #iterating through each character in plainText string
    for char in plainText:
        char = encryptCharacter(char, a ,b)
        cipherText = cipherText + char
    return cipherText

def encryptCharacter(char, a, b):
    #checks if character is in alphabet
    if(char in alphabet.values()): 
        newChar = alphabet.get((a * ord(char)  + b) % 26)
        return newChar
    #if character is not in alphabet return plain character
    else:
        return char


plainText = "HELLO WORLD!"
print(encryptAffine(plainText, 1, 1))
print(alphabet)