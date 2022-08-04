# Required modules
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def findCiphertext():
    messageA = b"I'll give you 500 and that's my last offer."
    messageB = b"I'll give you 100 and that's my last offer."
    messageACipherText =  b"\xef@\x92<$J\xb2\x8c\xbc\xabl'\x016\xd2{W-8\xcas\x83*\xa1\xef)\xc0\xda\x7fe\xab\xb1\x94\x7fJ\x98\xc8\xeei|'t\xb4"
    messageBCipherText = byte_xor(messageACipherText, byte_xor(messageA, messageB))
    return messageBCipherText

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])