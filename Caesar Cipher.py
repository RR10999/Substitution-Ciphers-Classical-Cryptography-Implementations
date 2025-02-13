def caesar_cipher(text, shift):
    return ''.join(chr((ord(c) - 65 + shift) % 26 + 65) if c.isalpha() else c for c in text.upper())

text = input("Enter plaintext: ")
shift = int(input("Enter shift: "))
print("Ciphertext:", caesar_cipher(text, shift))
