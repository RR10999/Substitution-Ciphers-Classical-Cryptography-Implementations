This repository contains implementations of substitution ciphers, a fundamental class of encryption techniques used in classical cryptography. These methods replace characters in plaintext with different characters based on a fixed or variable key. While not secure by modern standards, they are essential for understanding cryptographic principles.
Ciphers Included
.Simple Substitution Ciphers:
Caesar Cipher – Shifts letters by a fixed amount.
Polyalphabetic Ciphers –  Uses multiple substitution alphabets to encrypt a message, making frequency analysis more difficult.
Monoalphabetic Cipher – Uses a scrambled alphabet for substitution.
.Digraph & Matrix-Based Ciphers:
Playfair Cipher – Encrypts letter pairs using a 5×5 key square.
Hill Cipher – Uses linear algebra & matrix multiplication.
Polyalphabetic Ciphers:
Vigenère Cipher – Uses a keyword-based shift.
Auto-Key Cipher – Extends Vigenère by adding plaintext to the key.
One-Time Pad (Vernam Cipher) – Theoretically unbreakable, using a random key as long as the message.
