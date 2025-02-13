def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:return i
    return None
def matrix_mult(mat, vec):
    return [(mat[0][0] * vec[0] + mat[0][1] * vec[1]) % 26,
            (mat[1][0] * vec[0] + mat[1][1] * vec[1]) % 26]
def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2:text += "X"
    result = ""
    for i in range(0, len(text), 2):
        vec = [ord(text[i]) - 65, ord(text[i+1]) - 65]
        enc_vec = matrix_mult(key, vec)
        result += chr(enc_vec[0] + 65) + chr(enc_vec[1] + 65)
    return result
def hill_decrypt(text, key):
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    det_inv = mod_inverse(det % 26, 26)
    if det_inv is None:return "Key is not invertible!"
    adjugate = [[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]
    inv_key = [[(det_inv * adjugate[i][j]) % 26 for j in range(2)] for i in range(2)]
    return hill_encrypt(text, inv_key)
key = []
print("Enter 2x2 key matrix:")
for i in range(2):
    key.append(list(map(int, input().split())))
plaintext = input("Enter plaintext: ").upper()
ciphertext = hill_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
print("Decrypted:", hill_decrypt(ciphertext, key))