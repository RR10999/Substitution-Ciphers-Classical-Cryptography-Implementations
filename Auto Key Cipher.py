def auto_key_cipher(text, key):
    key = (key + text).upper()[:len(text)]
    return ''.join(chr((ord(t) + ord(k) - 2*65) % 26 + 65) if t.isalpha() else t for t, k in zip(text.upper(), key))

text = input("Enter plaintext: ")
key = input("Enter key: ")
print("Ciphertext:", auto_key_cipher(text, key))
