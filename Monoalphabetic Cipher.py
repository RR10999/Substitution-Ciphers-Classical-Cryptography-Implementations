import string
import random

def monoalphabetic_cipher(text):
    letters = string.ascii_uppercase
    shuffled = list(letters)
    random.shuffle(shuffled)
    mapping = dict(zip(letters, shuffled))
    return ''.join(mapping.get(c, c) for c in text.upper())

text = input("Enter plaintext: ")
print("Ciphertext:", monoalphabetic_cipher(text))
