import numpy as np

def hill_cipher(text, key):
    text = text.upper().replace(" ", "")
    n = int(len(key) ** 0.5)
    key_matrix = np.array([[ord(c) - ord('A') for c in key[i*n:(i+1)*n]] for i in range(n)])
    text_vector = [ord(c) - ord('A') for c in text]
    
    while len(text_vector) % n != 0:
        text_vector.append(ord('X') - ord('A'))
    
    result = ""
    for i in range(0, len(text_vector), n):
        chunk = np.array(text_vector[i:i+n])
        cipher_chunk = key_matrix.dot(chunk) % 26
        result += "".join(chr(c + ord('A')) for c in cipher_chunk)
    return result

text = input("Enter the text: ")
key = input("Enter key for Hill Cipher (4-letter for 2*2 matrix): ")
print("Hill Cipher Output:", hill_cipher(text, key))
