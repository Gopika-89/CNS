from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_pin(pin, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce 
    ciphertext, tag = cipher.encrypt_and_digest(pin.encode())
    return base64.b64encode(nonce + ciphertext).decode()

def decrypt_pin(encrypted_pin, key):
    raw = base64.b64decode(encrypted_pin)
    nonce, ciphertext = raw[:16], raw[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()

aes_key = get_random_bytes(16)
pin = "1234"
encrypted_pin = encrypt_pin(pin, aes_key)
print("Encrypted PIN:", encrypted_pin)
decrypted_pin = decrypt_pin(encrypted_pin, aes_key)
print("Decrypted PIN:", decrypted_pin)
# Authentication Check
if decrypted_pin == pin:
    print("Authentication Successful!")
else:
    print("Authentication Failed!")
