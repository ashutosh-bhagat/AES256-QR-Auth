# backend/encryptor.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

# ✅ AES-256 key (must be 32 bytes)
SECRET_KEY = b'This_is_32_byte_secret_key__123!'  # Length = 32

def encrypt_data(data: str) -> str:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Padding to make data multiple of 16 bytes (PKCS7 style)
    padded_data = data.encode()
    padding_len = 16 - (len(padded_data) % 16)
    padded_data += bytes([padding_len]) * padding_len

    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    return base64.urlsafe_b64encode(iv + encrypted).decode()