#!/usr/bin/python2

from __future__ import division
import math as m
import string
import sys

def contFract(N):
    while True:
        yield N//1
        f = N - (N//1)
        if f < 0.00001:
            break
        N = 1/f

def unique_in_list(list_numbers):

    uniques = []

    for i in xrange(len(list_numbers)):
        if list_numbers[i] not in uniques:
            uniques.append(list_numbers[i])

    return uniques

def inv_map(f):
    return f.__class__(map(reversed, f.items()))


def main():

    # Separate a list to store the sequence.

    sequence = []

    # Store the sequence in order to order the leters.

    sequence = list(contFract(m.sqrt(2.0)))

    # Define an alphabet.

    alphabet = list(string.ascii_lowercase)

    # Define the uncrypt messgae.

    u_msg = "i hate waking up early"

    # Get unique list of numbers from periodic fraction list.

    alph_map = unique_in_list(sequence)

    if (len(alph_map) < 26):
        sys.exit("ERROR: You need at least 26 numbers for alphabet maping.")

    # Now, lets get the mapping, but first, map the spaces.

    alphabet.append(" ")

    # Lets build a dictionaru with our maps.

    cryp_dic = dict(zip(alphabet, alph_map[0:27]))

    # Crypt our message brow !

    crypt_message = []

    for i in xrange(len(u_msg)):
        print cryp_dic[u_msg[i]]
        crypt_message.append(cryp_dic[u_msg[i]])

    # Uncrypt the message.

    cryp_dic = inv_map(cryp_dic)

    for i in xrange(len(crypt_message)):
        print cryp_dic[crypt_message[i]]
        
if __name__== "__main__":
    main()

