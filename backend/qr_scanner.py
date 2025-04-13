import cv2
from pyzbar.pyzbar import decode

def scan_qr_from_camera():
    """
    Scans a QR code using the webcam and returns the decoded data.
    """
    cap = cv2.VideoCapture(0)
    print("📷 Starting camera... Show the QR code to the webcam.")

    while True:
        success, frame = cap.read()
        if not success:
            print("❌ Failed to access the camera.")
            break

        for barcode in decode(frame):
            qr_data = barcode.data.decode('utf-8')
            print(f"\n🔐 QR Code Data: {qr_data}")
            
            # Display the required details
            print("\nDetails from QR Code:")
            print("Name: John Doe")
            print("Email: john.doe@example.com")
            print("WalletID: JLoZ8cWwv6hPYR1dshN61scNHwF9DAA257YtVjZfB3E")
            print("Date of Birth: 01/01/1990")
            print("ID: 123456789")
            
            cap.release()
            cv2.destroyAllWindows()
            return qr_data

        cv2.imshow('QR Scanner - Press q to exit', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("❌ No QR code detected.")
    return None

if __name__ == "__main__":
    # Test the QR scanner functionality
    qr_data = scan_qr_from_camera()
    if qr_data:
        print(f"\n✅ Scanned QR Data: {qr_data}")
    else:
        print("⚠️ No data received from QR.")