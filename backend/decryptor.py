# backend/decryptor.py

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# ✅ Must match the key in encryptor.py
SECRET_KEY = b'This_is_32_byte_secret_key__123!'

def decrypt_data(encrypted_data_b64: str) -> str:
    try:
        encrypted_data = base64.urlsafe_b64decode(encrypted_data_b64)
        iv = encrypted_data[:16]
        encrypted_message = encrypted_data[16:]

        cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_padded = decryptor.update(encrypted_message) + decryptor.finalize()
        padding_length = decrypted_padded[-1]
        decrypted_data = decrypted_padded[:-padding_length].decode('utf-8')

        return decrypted_data
    except Exception as e:
        return f"❌ Decryption failed: {str(e)}"