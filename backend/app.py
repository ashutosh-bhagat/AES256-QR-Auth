# backend/app.py
from flask import Flask, request, jsonify
from decryptor import decrypt_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend access

@app.route("/verify", methods=["POST"])
def verify_qr():
    data = request.get_json()
    encrypted_str = data.get("encrypted")

    try:
        decrypted = decrypt_data(encrypted_str)
        return jsonify({
            "success": True,
            "message": "Decryption successful",
            "data": decrypted
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Decryption failed: {str(e)}"
        }), 400

if __name__ == "__main__":
    app.run(debug=True)