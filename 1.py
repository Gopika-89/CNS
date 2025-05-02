def playfair_cipher(text, key):
    text = text.upper().replace("J", "I").replace(" ", "")
    key = key.upper().replace("J", "I")
    matrix = "".join(sorted(set(key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"), key=lambda x: (key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").index(x)))
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    
    def get_pos(letter):
        for r, row in enumerate(matrix):
            if letter in row:
                return r, row.index(letter)

    pairs = []
    i = 0
    while i < len(text):
        if i+1 < len(text) and text[i] != text[i+1]:
            pairs.append(text[i] + text[i+1])
            i += 2
        else:
            pairs.append(text[i] + 'X')
            i += 1
    
    result = ""
    for a, b in pairs:
        r1, c1 = get_pos(a)
        r2, c2 = get_pos(b)
        if r1 == r2:
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

text = input("Enter the text: ")
key = input("Enter key for Playfair Cipher: ")
print("Playfair Cipher Output:", playfair_cipher(text, key))
