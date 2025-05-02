from Crypto.Cipher import AES
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '  # Padding to make text a multiple of 16
    return text

def aes_encrypt(plain_text, key):
    key = key[:16]  # AES key must be 16, 24, or 32 bytes long
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted_text).decode()

def aes_decrypt(cipher_text, key):
    key = key[:16]  # AES key must be 16, 24, or 32 bytes long
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(cipher_text)).decode()
    return decrypted_text.strip()

# Input from the user
plain_text = input("Enter text to encrypt: ")
key = input("Enter a 16-character key: ")

# Encrypt and decrypt
encrypted_text = aes_encrypt(plain_text, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = aes_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
