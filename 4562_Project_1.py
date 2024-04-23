import binascii

def simple_des_permutation(key, plaintext):
    # Simplified permutation function for encryption
    return ''.join([chr((ord(plaintext[i]) + ord(key[i % len(key)])) % 256) for i in range(len(plaintext))])

def simple_des_inverse_permutation(key, ciphertext):
    # Simplified permutation function for decryption
    return ''.join([chr((ord(ciphertext[i]) - ord(key[i % len(key)])) % 256) for i in range(len(ciphertext))])

def simple_des_encryption(key, plaintext):
    # Simplified encryption function
    ciphertext = ''
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        for _ in range(16):  
            block = simple_des_permutation(key, block)
        ciphertext += block
    return binascii.hexlify(ciphertext.encode()).decode()

def simple_des_decryption(key, ciphertext):
    # Simplified decryption function
    plaintext = ''
    ciphertext = binascii.unhexlify(ciphertext).decode('utf-8', 'ignore')
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]
        for _ in range(16):  
            block = simple_des_inverse_permutation(key, block)
        plaintext += block
    return plaintext


# Test the encryption function
plaintext = 'plaintext test'
key = '0123456789abcdef'
print(f'Plaintext: {plaintext}')
print(f'Key: {key}')
ciphertext = simple_des_encryption(key, plaintext)
print(f'Ciphertext: {ciphertext}')

# Test the decryption function
decrypted_plaintext = simple_des_decryption(key, ciphertext)
print(f'Decrypted plaintext: {decrypted_plaintext}')
