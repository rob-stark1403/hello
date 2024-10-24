# CODE:
import random

# Helper function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Extended Euclidean Algorithm to find modular inverse
def mod_inverse(e, phi_n):
    g, x, _ = extended_gcd(e, phi_n)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi_n

# Helper function to compute gcd and coefficients (x, y)
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

# Function to compute gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# RSA Key generation (with user input for p and q)
def generate_rsa_keys():
    # Step 1: Input two prime numbers from the user
    p = int(input("Enter a prime number p: "))
    while not is_prime(p):
        p = int(input("p is not a prime number. Please enter a prime number p: "))

    q = int(input("Enter a prime number q: "))
    while not is_prime(q) or q == p:
        q = int(input("q is either not a prime number or same as p. Please enter another prime number q: "))

    # Step 2: Compute n = p * q
    n = p * q

    # Step 3: Compute φ(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)

    # Step 4: Use a fixed e, commonly 65537
    e = 65537
    # Check if gcd(e, φ(n)) = 1
    if gcd(e, phi_n) != 1:
        raise Exception('e and φ(n) are not coprime, please choose different p and q')

    # Step 5: Compute d, the modular inverse of e mod φ(n)
    d = mod_inverse(e, phi_n)

    return (e, n), (d, n)  # (Public key, Private key)

# RSA encryption
def encrypt_rsa(plaintext, public_key):
    e, n = public_key
    # Ensure plaintext is less than n
    if plaintext >= n:
        raise ValueError("Plaintext must be less than n.")
    ciphertext = pow(plaintext, e, n)
    return ciphertext

# RSA decryption
def decrypt_rsa(ciphertext, private_key):
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext

# Main RSA logic
if __name__ == "__main__":
    print("RSA Algorithm Implementation")

    # Generate RSA keys (with user inputs for p and q)
    public_key, private_key = generate_rsa_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Take plaintext input from user
    plaintext = int(input("Enter the plaintext (integer less than n) to encrypt: "))

    # Encrypt the plaintext
    ciphertext = encrypt_rsa(plaintext, public_key)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt_rsa(ciphertext, private_key)
    print(f"Decrypted Plaintext: {decrypted_text}")
