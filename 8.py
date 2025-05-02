def vigenere_cipher(text, key):
    result = ""
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            new_char = chr(((ord(char.upper()) - ord('A') + shift) % 26) + ord('A'))
            result += new_char.lower() if char.islower() else new_char
        else:
            result += char
    return result

text = input("Enter the text: ")
key = input("Enter key for Vigenere Cipher: ")
print("Vigenere Cipher Output:", vigenere_cipher(text, key))
