# backend/encryptor.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

# MUST be exactly 32 bytes
SECRET_KEY = b'\xa2\xf1...your 32-byte-key...'  # use os.urandom(32) to generate one

def encrypt_data(data: str) -> str:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padded_data = data.encode()
    padded_data += b"\0" * (16 - len(padded_data) % 16)

    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    return base64.urlsafe_b64encode(iv + encrypted).decode()

def decrypt_data(encrypted_data: str) -> str:
    raw = base64.urlsafe_b64decode(encrypted_data)
    iv = raw[:16]
    encrypted = raw[16:]
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted) + decryptor.finalize()
    return decrypted.rstrip(b"\0").decode()