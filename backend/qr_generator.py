# backend/qr_generator.py

import qrcode
from encryptor import encrypt_data

data_to_encrypt = "Ashu_Authenticated"  # 🔐 Replace this with real payload
encrypted_data = encrypt_data(data_to_encrypt)

# ✅ Save QR Code
img = qrcode.make(encrypted_data)
img.save("qr.png")
print("[✅] QR code generated and saved as qr.png")