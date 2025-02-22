def caesar_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():  
            shift = 3
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  
    return result

def caesar_cipher_decryption(ciphertext):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 3
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

text = input("Enter plaintext: ")
ciphertext = caesar_cipher(text)
print("Ciphertext:", ciphertext)

plaintext = caesar_cipher_decryption(ciphertext)
print("Decrypted Plaintext:", plaintext)
