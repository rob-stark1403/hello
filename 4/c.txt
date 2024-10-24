# Function to encrypt the plain text using Vigenere Cipher
def vig_encrypt(plain, key):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ""
    key_len = len(key)
    key = key.upper()
    plain = plain.upper()
   
    for i in range(len(plain)):
        if plain[i].isalpha():  # Only process alphabet characters
            p = letters.index(plain[i])
            k = letters.index(key[i % key_len])
            c = (p + k) % 26
            cipher += letters[c]
        else:
            cipher += plain[i]  # Append non-alphabet characters as is
   
    return cipher

# Function to decrypt the cipher text using Vigenere Cipher
def vig_decrypt(cipher, key):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain = ""
    key_len = len(key)
    key = key.upper()
    cipher = cipher.upper()
   
    for i in range(len(cipher)):
        if cipher[i].isalpha():  # Only process alphabet characters
            c = letters.index(cipher[i])
            k = letters.index(key[i % key_len])
            p = (c - k) % 26
            plain += letters[p]
        else:
            plain += cipher[i]  # Append non-alphabet characters as is
   
    return plain

# Main execution
plain = input("Enter the plain text: ").strip()
key = input("Enter the key: ").strip()

# Encrypting the plain text
cipher = vig_encrypt(plain, key)
print("Encrypted cipher:", cipher)

# Decrypting the cipher text
decrypted_text = vig_decrypt(cipher, key)
print("Decrypted plain text:", decrypted_text)
