# CODE:
import numpy as np

# Function to create the 5x5 matrix for the cipher
def create_matrix(key):
    key = key.upper().replace("J", "I")  # Replace J with I
    matrix = []
    for char in key:
        if char not in matrix and char.isalpha():
            matrix.append(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is excluded
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    matrix_5x5 = np.array(matrix).reshape(5, 5)
    return matrix_5x5

# Function to find the position of a character in the matrix
def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

# Function to format the plaintext into digraphs (pairs of two letters)
def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared_text = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text):
            char2 = text[i + 1]
        else:
            char2 = 'X'
        
        if char1 == char2:
            prepared_text += char1 + 'X'
            i += 1
        else:
            prepared_text += char1 + char2
            i += 2
    
    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'
    
    return prepared_text

# Playfair encryption function
def encrypt(plaintext, key):
    matrix = create_matrix(key)
    prepared_text = prepare_text(plaintext)
    
    ciphertext = ""
    
    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    
    return ciphertext

# Playfair decryption function
def decrypt(ciphertext, key):
    matrix = create_matrix(key)
    
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    
    return plaintext

# Main function to run the Playfair Cipher
def main():
    key = input("Enter the key for the cipher: ")
    plaintext = input("Enter the plaintext to encrypt: ")
    
    ciphertext = encrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
    
    decrypted_text = decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")

# Run the program
main()
