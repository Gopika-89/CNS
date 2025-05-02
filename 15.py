def rail_fence_encrypt(text, rails):
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(text)):
        fence[rail][i] = text[i]
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    result = []
    for row in fence:
        result.extend([char for char in row if char != '\n'])
    
    return "".join(result)

def rail_fence_decrypt(cipher_text, rails):
    fence = [['\n' for _ in range(len(cipher_text))] for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(cipher_text)):
        fence[rail][i] = '*'
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0
    for row in range(rails):
        for col in range(len(cipher_text)):
            if fence[row][col] == '*' and index < len(cipher_text):
                fence[row][col] = cipher_text[index]
                index += 1

    result = []
    rail = 0
    direction = 1

    for i in range(len(cipher_text)):
        result.append(fence[rail][i])
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return "".join(result)

text = input("Enter the text: ")
rails = int(input("Enter number of rails: "))

cipher_text = rail_fence_encrypt(text, rails)
print("Encrypted Text:", cipher_text)

decrypted_text = rail_fence_decrypt(cipher_text, rails)
print("Decrypted Text:", decrypted_text)
