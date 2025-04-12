# backend/qr_generator.py

import qrcode
from encryptor import encrypt_data

def generate_qr(user_data: dict, filename="qr.png"):
    # Convert user data to string
    data_str = f"{user_data['name']}|{user_data['email']}|{user_data['timestamp']}"
    
    # Encrypt the data
    encrypted = encrypt_data(data_str)

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(encrypted)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")