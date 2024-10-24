# CODE:
def caesar_cipher(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

def print_table(columns, key):
    print(' '.join(key))
    print(' '.join('-' * len(char) for char in key))
    for i in range(len(columns[0])):
        row = ''
        for j in range(len(columns)):
            if i < len(columns[j]):
                row += columns[j][i] + ' '
            else:
                row += '  '
        print(row)
    print()

def columnar_transposition_encrypt(plaintext, key):
    num_cols = len(key)
    num_rows = -(-len(plaintext) // num_cols) 
    padded_text = plaintext.ljust(num_rows * num_cols, 'X') 

    columns = ['' for _ in range(num_cols)]
    for i, char in enumerate(padded_text):
        columns[i % num_cols] += char

    print("Encryption Table:")
    print_table(columns, key)

    key_order = sorted(range(num_cols), key=lambda x: key[x])
    return ''.join(columns[i] for i in key_order)

plaintext =  input("Enter the plaintext: ")
shift = int(input("Enter the number for shift : "))
encrypted_text = caesar_cipher(plaintext, shift)
print(f"Encrypted: {encrypted_text}")

key = input("Enter the key (COLUMNAR): ")
encrypted = columnar_transposition_encrypt(encrypted_text, key)
print("Final Encrypted Message: " + encrypted)
