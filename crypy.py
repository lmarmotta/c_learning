#!/usr/bin/python3

from __future__ import division
from __future__ import print_function, unicode_literals
from random import randint
from os import urandom
import math as m
import string
import sys

# 
# Generate binnary randons.
#

def genbyte(length):
    return urandom(length)

#
# Generate rangdom numbers.
#

def genran(length):
    num_list = []
    for i in range(length):
        num_list.append(randint(0,300))
    return num_list

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
# Special function to xor two strings.
#

def xor_strings(s, t):
    """xor two strings together"""
    if isinstance(s, str):
        # Text strings contain single characters
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Python 3 bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])

def main():

    # Define a key.

    key_seed    = 23.1
    garb_length = 100
    jump        = 2

    # Create the key.

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

    print ("+ Clear message: ", clear_message_byte, "\n")
    print ("+ The Key: ", crypt_message_byte,"\n")

    crypt_message_safe = xor_strings(clear_message_byte, crypt_message_byte)

    print ("+ Crypt message (core): ", crypt_message_safe,"\n")

    crypt_message_safe = crypt_message_safe + genbyte(garb_length)

    print ("+ Crypt message (core + backward trash): ", crypt_message_safe,"\n")

    crypt_message_safe = genbyte(garb_length) + crypt_message_safe 

    print ("+ Crypt message (backward trash + trashed message): ", crypt_message_safe,"\n")

    file_out = open("test.dat","w")
    for i in range(len(crypt_message_safe)):
        file_out.write(str(crypt_message_safe[i])) # dieharder -a -f test.dat
    file_out.close()

    # Append trash to message.

    crypt_message_safe = xor_strings(crypt_message_safe[garb_length:garb_length + len(clear_message)], crypt_message_byte)

    print ("+ Decrypted message: ", crypt_message_safe.decode('utf8'),"\n")

if __name__== "__main__":
    main()

