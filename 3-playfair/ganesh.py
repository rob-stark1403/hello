import re

def parse_string(input_str):
    parse = input_str.upper()
    parse = re.sub(r'[^A-Z]', '', parse)
    parse = parse.replace('J', 'I')
    return parse

def cipher_table(key):
    key_string = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    playfair_table = [["" for _ in range(5)] for _ in range(5)]
    
    used = set()
    k = 0
    for char in key_string:
        if char not in used:
            used.add(char)
            playfair_table[k // 5][k % 5] = char
            k += 1
    
    return playfair_table

def insert_x_between_double_letters(text, length):
    for i in range(0, length - 1):
        if text[2 * i] == text[2 * i + 1]:
            text = text[:2 * i + 1] + 'X' + text[2 * i + 1:]
            length = len(text) // 2 + len(text) % 2
    if len(text) % 2 == 1:
        text += 'X'
    return text

def create_digraphs(text, length):
    return [text[2 * i] + text[2 * i + 1] for i in range(length)]

def get_point(table, char):
    for i in range(5):
        for j in range(5):
            if table[i][j] == char:
                return (i, j)
    return None

def encode_digraph(table, digraphs, length):
    enciphered = []
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        r1, c1 = get_point(table, a)
        r2, c2 = get_point(table, b)

        if r1 == r2:
            c1 = (c1 + 1) % 5
            c2 = (c2 + 1) % 5
        elif c1 == c2:
            r1 = (r1 + 1) % 5
            r2 = (r2 + 1) % 5
        else:
            c1, c2 = c2, c1

        enciphered.append(table[r1][c1] + table[r2][c2])
    return enciphered

def decode(table, text):
    decoded = []
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = get_point(table, a)
        r2, c2 = get_point(table, b)

        if r1 == r2:
            c1 = (c1 + 4) % 5
            c2 = (c2 + 4) % 5
        elif c1 == c2:
            r1 = (r1 + 4) % 5
            r2 = (r2 + 4) % 5
        else:
            c1, c2 = c2, c1

        decoded.append(table[r1][c1] + table[r2][c2])
    return ''.join(decoded)

def key_table(table):
    print("Playfair Cipher Key Matrix:")
    print()
    for row in table:
        print(" ".join(row))
    print()

def print_results(enciphered, deciphered):
    print("Encrypted Message: " + enciphered)
    print()
    print("Decrypted Message: " + deciphered)


key = parse_string(input("Enter the key for playfair cipher: "))
while key == "":
    key = parse_string(input("Enter the key for playfair cipher: "))
    
table = cipher_table(key)
    
plaintext = parse_string(input("Enter the plaintext to be enciphered: "))
while plaintext == "":
    plaintext = parse_string(input("Enter the plaintext to be enciphered: "))

length = len(plaintext) // 2 + len(plaintext) % 2
plaintext = insert_x_between_double_letters(plaintext, length)
digraphs = create_digraphs(plaintext, length)
enciphered = ''.join(encode_digraph(table, digraphs, length))
decoded = decode(table, enciphered)

key_table(table)
print_results(enciphered, decoded)