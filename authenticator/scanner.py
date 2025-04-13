import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from decryptor import decrypt_data
# authenticator/scanner.py

import cv2
from pyzbar.pyzbar import decode
from decryptor import decrypt_data

def scan_qr():
    print("[DEBUG] Starting scanner...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Cannot access webcam.")
        return

    print("[INFO] Webcam opened successfully. Looking for QR codes...")
    while True:
        success, frame = cap.read()
        if not success:
            continue

        for barcode in decode(frame):
            qr_data = barcode.data.decode('utf-8')
            print("[INFO] QR code detected")

            # ✅ Decrypt QR data
            decrypted = decrypt_data(qr_data)
            print("✅ Decrypted Data:", decrypted)

            cap.release()
            cv2.destroyAllWindows()
            return

        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr()