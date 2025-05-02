def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

text = input("Enter the text: ")
shift = int(input("Enter shift for Caesar Cipher: "))
print("Caesar Cipher Output:", caesar_cipher(text, shift))
