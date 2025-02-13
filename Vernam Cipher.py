import random

def vernam_cipher(text):
    key = ''.join(chr(random.randint(65, 90)) for _ in text)
    cipher = ''.join(chr((ord(t) ^ ord(k)) + 65) for t, k in zip(text.upper(), key))
    return key, cipher

text = input("Enter plaintext: ")
key, ciphertext = vernam_cipher(text)
print("Key:", key)
print("Ciphertext:", ciphertext)
