def caesar_encrypt(text, shift):
    """Encrypts text using the Caesar cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    """Decrypts text encrypted with the Caesar cipher."""
    return caesar_encrypt(text, -shift)  # Decryption is just encryption with a negative shift

# Get user input
plaintext = input("Enter the text to encrypt: ")
shift_key = int(input("Enter the shift key (number): "))

# Encrypt and decrypt
encrypted_text = caesar_encrypt(plaintext, shift_key)
print("Encrypted Text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift_key)
print("Decrypted Text:", decrypted_text)
