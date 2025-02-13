def polyalphabetic_cipher(text, keys):
    keys = [int(k) for k in keys.split()]
    return ''.join(chr((ord(c) - 65 + keys[i % len(keys)]) % 26 + 65) if c.isalpha() else c for i, c in enumerate(text.upper()))

text = input("Enter plaintext: ")
keys = input("Enter space-separated shift values: ")
print("Ciphertext:", polyalphabetic_cipher(text, keys))