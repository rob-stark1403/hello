# pip install pycryptodomex

from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

# DES block size is 8 bytes
BLOCK_SIZE = 8

# DES encryption function
def encrypt_des(plain_text, key):
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(BLOCK_SIZE)
    
    # Create a new DES cipher in CBC mode
    cipher = DES.new(key, DES.MODE_CBC, iv)
    
    # Pad the plain text to be a multiple of the block size
    padded_text = pad(plain_text.encode(), BLOCK_SIZE)
    
    # Encrypt the padded plain text
    encrypted_text = cipher.encrypt(padded_text)
    
    # Return the IV and encrypted text concatenated
    return iv + encrypted_text

# DES decryption function
def decrypt_des(encrypted_text, key):
    # Extract the IV from the beginning of the encrypted text
    iv = encrypted_text[:BLOCK_SIZE]
    
    # Extract the actual encrypted text
    actual_encrypted_text = encrypted_text[BLOCK_SIZE:]
    
    # Create a new DES cipher in CBC mode using the same IV
    cipher = DES.new(key, DES.MODE_CBC, iv)
    
    # Decrypt the encrypted text and remove the padding
    decrypted_text = unpad(cipher.decrypt(actual_encrypted_text), BLOCK_SIZE)
    
    # Return the decrypted text as a string
    return decrypted_text.decode()

# Test the DES encryption and decryption
if __name__ == "__main__": 
    # 8 bytes (64 bits) key for DES
    key = get_random_bytes(8)

    # Plain text message
    message = "Rob Stark"
    
    # Encrypt the message
    encrypted_message = encrypt_des(message, key)
    print(f"Encrypted message: {encrypted_message.hex()}")
    
    # Decrypt the message
    decrypted_message = decrypt_des(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")
