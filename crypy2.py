#!/usr/bin/python3

from __future__ import division
from __future__ import print_function, unicode_literals
from random import randint
from os import urandom
import math as m
import string
import sys
import random
from utils import * # From https://github.com/pBouillon/rsa

# 
# Generate binnary randons.
#

def genbyte(length):
    return urandom(length)

#
# Expand number by continuous fractions.
#

def genkey(N):
    while True:
        yield N//1
        f = N - (N//1)
        if f < 0.0001:
            break
        N = 1/f

#
# Keypair generator.
#

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    
    return ((e, n), (d, n))

#
# Special function to xor two strings.
#

def xor_strings(s, t):
    """xor two strings together"""
    if isinstance(s, str):
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        return bytes([a ^ b for a, b in zip(s, t)])

def main():

    # -- SENDER ACTIONS --

    # Create the expansion key.

    key_seed    = 23.1

    # Set the garbage length (each side).

    garb_length = 100

    # Set the jump in the extension key.

    jump        = 2

    # Set the message.

    clear_message = "This is a cool message which cannot be seen !!"

    # Generate the key of 

    key = list(genkey(m.sqrt(key_seed)))

    # Check the size of the key in relation to the message.

    if (len(clear_message) > jump**len(key)):
        sys.exit("ERROR: You need a better seed")

    # Select the key due to jump.

    zkey = []

    for i in range(0,len(key),jump):
        zkey.append(key[i])

    # Separate the size of the key == message.

    zkey_ms = zkey[0:len(clear_message)]

    # Convert byte arrays.

    clear_message_byte = clear_message.encode('utf8')
    crypt_message_byte = ' '.join(map(str,zkey_ms)).encode('utf8')

    # Dump text.

    print ("+ Clear message: ", clear_message_byte, "\n")

    print ("+ The Key: ", crypt_message_byte,"\n")

    # Cipher the message.

    crypt_message_safe = xor_strings(clear_message_byte, crypt_message_byte)

    # Dump text.

    print ("+ Crypt message (core): ", crypt_message_safe,"\n")

    # Append Garbage.

    crypt_message_safe = crypt_message_safe + genbyte(garb_length)

    print ("+ Crypt message (core + backward trash): ", crypt_message_safe,"\n")

    # Send this message.

    crypt_message_safe = genbyte(garb_length) + crypt_message_safe

    print ("+ Crypt message (backward trash + trashed message): ", crypt_message_safe,"\n")

    file_out = open("test.dat","w")
    for i in range(len(crypt_message_safe)):
        file_out.write(str(crypt_message_safe[i])) # dieharder -a -f test.dat
    file_out.close()

    # Now, prepare the key to be send. Convert key to string.

    key_infos = str(key_seed) + ',' + str(garb_length) + ',' + str(jump)

    # Encript the keys infos with rsa.

    p = get_rdm_prime_nb()
    q = get_rdm_prime_nb(to_ignore=[p])

    pub_k, priv_k = gen_keys(p, q)

    ciphertext = encrypt(pub_k, key_infos)

    # -- RECEIVER ACTIONS --

    # Decript the key infos.

    d_key_infos = decrypt(priv_k, ciphertext)

    # Build infra structure.

    list_param = d_key_infos.split(",")

    # Separate parameters.

    key_seed    = float(list_param[0])
    garb_length = int(list_param[1])
    jump        = int(list_param[2])

    # Generate the key of 

    key = list(genkey(m.sqrt(key_seed)))

    # Check the size of the key in relation to the message.

    if (len(clear_message) > jump**len(key)):
        sys.exit("ERROR: You need a better seed")

    # Select the key due to jump.

    zkey = []

    for i in range(0,len(key),jump):
        zkey.append(key[i])

    # Separate the size of the key == message.

    zkey_ms = zkey[0:len(clear_message)]

    # Convert byte arrays.

    crypt_message_byte = ' '.join(map(str,zkey_ms)).encode('utf8')

    # Decript message

    crypt_message_safe = xor_strings(crypt_message_safe[garb_length:garb_length + len(clear_message)], crypt_message_byte)

    print ("+ Decrypted message: ", crypt_message_safe.decode('utf8'),"\n")

if __name__== "__main__":
    main()

