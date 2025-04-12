# backend/test_qr.py

from qr_generator import generate_qr
import datetime

user_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "timestamp": datetime.datetime.now().isoformat()
}

generate_qr(user_data)