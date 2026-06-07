def generate_key(text, key):
    key = key.upper()
    new_key = ""

    for i in range(len(text)):
        new_key += key[i % len(key)]

    return new_key


def vigenere_encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = generate_key(text, key)

    cipher = ""

    for i in range(len(text)):
        x = (ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26
        cipher += chr(x + ord('A'))

    return cipher


def vigenere_decrypt(cipher, key):
    key = generate_key(cipher, key)

    plain = ""

    for i in range(len(cipher)):
        x = (ord(cipher[i]) - ord('A') - (ord(key[i]) - ord('A')) + 26) % 26
        plain += chr(x + ord('A'))

    return plain


# Main
text = input("Enter Plaintext: ")
key = input("Enter Keyword: ")

cipher = vigenere_encrypt(text, key)
print("Encrypted Text:", cipher)

plain = vigenere_decrypt(cipher, key)
print("Decrypted Text:", plain)