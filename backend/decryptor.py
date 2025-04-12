from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Same secret key used in encryption (must be 32 bytes for AES-256)
SECRET_KEY = b'This_is_a_32_byte_secret_key_1234'  # Replace with your actual 32-byte key

def decrypt_data(encrypted_data_b64: str) -> str:
    try:
        # Decode base64
        encrypted_data = base64.b64decode(encrypted_data_b64)

        # Extract IV (first 16 bytes)
        iv = encrypted_data[:16]
        encrypted_message = encrypted_data[16:]

        # Create AES cipher
        backend = default_backend()
        cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()

        # Decrypt and remove padding
        decrypted_padded = decryptor.update(encrypted_message) + decryptor.finalize()
        padding_length = decrypted_padded[-1]
        decrypted_data = decrypted_padded[:-padding_length].decode('utf-8')

        return decrypted_data

    except Exception as e:
        return f"❌ Decryption failed: {str(e)}"