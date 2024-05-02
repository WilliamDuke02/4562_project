# using fermats little theorum by checking if 2 ^ n-1 is congruent to 1 % n
# while this test is 100% i doubt we will run into edge cases in this impementation
def fermat_primechecker(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        return pow(2, n-1, n) == 1

# finds an array of primes inbetween start and end at the listed indicies
# ie find_primes(1000, 10000, [10, 19]) will return the 10th and 19th primes
def find_primes(start, end, indices):
    primes = []
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                primes.append(i)
            if len(primes) == max(indices):
                break
    return [primes[j - 1] for j in indices]

def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b , a % b
    return a  

#found on stackoverflow to compute modular inverse
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

# uses above func to determine the modular inverse found this on a 
# stackoverflow board (in .math but didnt want to use import)
def mod_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def find_e(p, q):
    phi = (p-1)*(q-1)
    e = 2
    while greatest_common_divisor(e, phi) != 1:
        e += 1
    return e

def find_publickey(e, p, q):
    n = p * q
    return [e, n]

def find_privatekey(e, p, q):
    phi = (p-1)*(q-1)
    d = mod_inverse(e, phi)
    return [d, p, q]

# encodes the message to characters a-z as 0-25
def encode_message(message):
    return [ord(char) - ord('a') for char in message.lower()]

def RSA_encrypt(message, publickey):
    e = publickey[0]
    n = publickey[1]
    return [pow(i, e, n) for i in message]

def RSA_decrypt(ciphertext, privatekey):
    n = privatekey[1]*privatekey[2]
    d = privatekey[0]
    return [pow(i, d, n) for i in ciphertext]

message = "rsa"
message = encode_message(message)
print(f"Encoded message: {message}")
primes = find_primes(1000, 10000, [10, 19])
p = primes[0]
q = primes[1]
e = find_e(p, q)
publickey = find_publickey(e, p, q)
print(f"Public Key: {publickey}")
privatekey = find_privatekey(e, p, q)
print(f"Private Key: {privatekey}")
ciphertext = RSA_encrypt(message, publickey)
print(f"Ciphertext: {ciphertext}")
checkmessage = RSA_decrypt(ciphertext, privatekey)
print(f"Decrypted Message: {checkmessage}")