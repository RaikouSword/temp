def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            matrix.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))

    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'

        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2

    if len(result) % 2:
        result += 'X'

    return result

def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = prepare_text(text)

    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

def playfair_decrypt(cipher, key):
    matrix = generate_key_matrix(key)

    plain = ""

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            plain += matrix[r1][(c1 - 1) % 5]
            plain += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:
            plain += matrix[(r1 - 1) % 5][c1]
            plain += matrix[(r2 - 1) % 5][c2]

        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain

# Main
key = input("Enter Key: ")
text = input("Enter Plaintext: ")

cipher = playfair_decrypt(text, key)
print("Encrypted:", cipher)

print("Decrypted:", playfair_decrypt(cipher, key))