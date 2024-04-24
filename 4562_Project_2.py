"""
Checklist ToDo
1) take user in and check if prime number
2) find 10th and 19th prime number (p and q) between 1000-10000
    Public key PU = {e,n}
    Private key PR = {d, p, q}
3) implement encipher and decipher for RSA
    test with "rsa" encode letters to (0-25)
4) show if adversary gets PU how exhaustive search to find private key d show time cost
"""

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
def find_primes(start, end, indicies):
    primes = []
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
                else:
                    primes.append(i)
            if len(primes) == max(indicies):
                break
        return [primes[j - 1] for j in indicies]

def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b , a % b
    return a  

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
    return [d, p, q]

def encode_message(message):
    return message

def RSA_encrypt(message, publickey):
    return ciphertext

def RSA_decrypt(ciphertext, privatekey):
    return message

message = "rsa"
message = encode_message(message)
primes = find_primes(1000, 10000, [10, 19])
p = primes[0]
q = primes[1]
e = find_e(p, q)
publickey = find_publickey(e, p, q)
print(publickey)
privatekey = find_privatekey(e, p, q)
print(privatekey)
ciphertext = RSA_encrypt(message, publickey)
print(ciphertext)
checkmessage = RSA_decrypt(ciphertext, privatekey)
print(checkmessage)