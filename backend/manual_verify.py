import base64
from encryptor import decrypt_data

def fix_padding(s):
    return s + '=' * ((4 - len(s) % 4) % 4)

# PASTE your string here:
raw_string = """gcLXPESm-QnVtD5-tRGmhvaqP0LRJCNKdXFGeWUv_gEKk7lU-ZqYUIkeFIBXOAiyRhlbrhKdHxaVzS42qmNIMZRgCO4e29uk_K5kxi4VCGg"""

try:
    fixed_string = fix_padding(raw_string)
    decrypted = decrypt_data(fixed_string)
    print(f"\n✅ Decrypted Data: {decrypted}")
except Exception as e:
    print(f"\n❌ Decryption failed: {e}")