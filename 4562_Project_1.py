import binascii

# This function performs a permutation operation on the plaintext using the key.
# It adds the ASCII value of each character in the plaintext and the corresponding character in the key (modulo 256),
# and then converts it back to a character. This operation is performed for each character in the plaintext.
def  des_permutation(key, plaintext):
    result = []
    for i in range(len(plaintext)):
        char = chr((ord(plaintext[i]) + ord(key[i % len(key)])) % 256)
        result.append(char)
    return ''.join(result)

# This function performs the inverse of the permutation operation on the ciphertext using the key.
# It subtracts the ASCII value of each character in the key from the corresponding character in the ciphertext (modulo 256),
# and then converts it back to a character. This operation is performed for each character in the ciphertext.
def  des_inverse_permutation(key, ciphertext):
    result = []
    for i in range(len(ciphertext)):
        char = chr((ord(ciphertext[i]) - ord(key[i % len(key)])) % 256)
        result.append(char)
    return ''.join(result)

# This function performs the DES encryption operation on the plaintext using the key.
# It divides the plaintext into blocks of 8 characters and performs the permutation operation 16 times on each block.
# The resulting ciphertext blocks are then concatenated and converted to hexadecimal.
def  des_encryption(key, plaintext):
    ciphertext = ''
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        for _ in range(16):  
            block =  des_permutation(key, block)
        ciphertext += block
    return binascii.hexlify(ciphertext.encode()).decode()

# This function performs the DES decryption operation on the ciphertext using the key.
# It first converts the ciphertext from hexadecimal to ASCII, then divides it into blocks of 8 characters,
# and performs the inverse permutation operation 16 times on each block. The resulting plaintext blocks are then concatenated.
def  des_decryption(key, ciphertext):
    plaintext = ''
    ciphertext = binascii.unhexlify(ciphertext).decode('utf-8', 'ignore')
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]
        for _ in range(16):  
            block =  des_inverse_permutation(key, block)
        plaintext += block
    return plaintext


# Test the encryption function
plaintext = 'plaintext test'
key = '0123456789abcdef'
print(f'Plaintext: {plaintext}')
print(f'Key: {key}')
ciphertext =  des_encryption(key, plaintext)
print(f'Ciphertext: {ciphertext}')

# Test the decryption function
decrypted_plaintext =  des_decryption(key, ciphertext)
print(f'Decrypted plaintext: {decrypted_plaintext}')