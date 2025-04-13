def load_key_iv():
    key = b'some_32_byte_key__________________'  # Should be 32 bytes for AES-256
    iv = b'some_16_byte_iv__'                   # Should be 16 bytes for AES block
    return key, iv