# Caesar Cipher - Encryption & Decryption

This repository contains a simple **Caesar Cipher** implementation in Python. The Caesar Cipher is a basic encryption technique where each letter in the plaintext is shifted by a fixed number.

## 📌 How It Works
1. The user enters the text to encrypt.
2. The user provides a shift key (number).
3. The program shifts each letter forward in the alphabet by the given key.
4. The program also provides decryption by shifting back.

## 🔹 Code Explanation
### Encryption (`caesar_encrypt` function)
- Each letter is shifted by the given key.
- If the shift goes past 'Z' or 'z', it wraps around using `% 26`.
- Non-alphabetic characters remain unchanged.

### Decryption (`caesar_decrypt` function)
- Decryption is simply encryption with the **negative shift**.

## 💻 Example Usage
```bash
Enter the text to encrypt: hello
Enter the shift key (number): 3
Encrypted Text: khoor
Decrypted Text: hello
