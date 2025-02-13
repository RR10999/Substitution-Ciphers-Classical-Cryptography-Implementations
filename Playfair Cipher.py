def generate_matrix(key):
    key = "".join(dict.fromkeys(key.replace("J", "I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
    return [list(key[i:i+5]) for i in range(0, 25, 5)]
def find_position(matrix, letter):
    for r, row in enumerate(matrix):
        if letter in row:return r, row.index(letter)
def process_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(filter(str.isalpha, text))
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:text = text[:i + 1] + "X" + text[i + 1:]
        i += 2
    if len(text) % 2 != 0:text += "X"
    return text
def playfair(text, key, encrypt=True):
    matrix = generate_matrix(key)
    text = process_text(text)
    result = ""
    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i+1])
        if r1 == r2:c1, c2 = (c1 + (1 if encrypt else -1)) % 5, (c2 + (1 if encrypt else -1)) % 5
        elif c1 == c2:r1, r2 = (r1 + (1 if encrypt else -1)) % 5, (r2 + (1 if encrypt else -1)) % 5
        else:c1, c2 = c2, c1
        result += matrix[r1][c1] + matrix[r2][c2]
    return result
key = input("Enter key: ").upper()
plaintext = input("Enter plaintext: ").upper()
ciphertext = playfair(plaintext, key)
print("Encrypted:", ciphertext)