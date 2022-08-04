# Required modules
import os
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_parameters, load_pem_public_key, load_pem_private_key
#from dhCheck import dhCheckCorrectness # You MUST have this included for your submission on Coderunner. You can remove it when you test your code in local system.



def Diffie_Hellman():
    parameters_raw = b'-----BEGIN DH PARAMETERS-----\nMEYCQQDP+dSNnBRy4jbHTvr0YcEk0bMzisMy+p/k9VYCb+gPNU/OSDkmEX62YKTc\nj1QrAo8+f3du/bjdfVKfv71LWtxjAgEC\n-----END DH PARAMETERS-----\n' 
    public_key_raw = b'-----BEGIN PUBLIC KEY-----\nMIGaMFMGCSqGSIb3DQEDATBGAkEAz/nUjZwUcuI2x0769GHBJNGzM4rDMvqf5PVW\nAm/oDzVPzkg5JhF+tmCk3I9UKwKPPn93bv243X1Sn7+9S1rcYwIBAgNDAAJAYyRw\n2K7KvbqudRx9DQtKH/tAQjDtDMIw7hFWYslMFnE/t44wArXQ/wuo0NPhFL4b63R8\nJZA7cF7tP+CAj3WHFA==\n-----END PUBLIC KEY-----\n'
    public_key = load_pem_public_key(public_key_raw, backend = default_backend())
    parameters = load_pem_parameters(parameters_raw, backend = default_backend())
    server_private_key = parameters.generate_private_key()
    server_public_key  = server_private_key.public_key()
    shared_key = server_private_key.exchange(public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend=default_backend()
    ).derive(shared_key)
    #key serialised to bytes, encoded with PEM, using typical public key format (SubjectPublicKeyInfo)
    pem_server_public_key  = server_public_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
    return pem_server_public_key, derived_key

print(Diffie_Hellman())