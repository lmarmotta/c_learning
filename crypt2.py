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

# Program call:
#
# ./crypt2.py <option> <input_file.txt> <key> <output_file.txt>
# 
# option == 0: Reads the file and crypts it with the key.
# option == 1: Reads the file and uncrypts it with the key.
#
# ./crypt2.py 0 input.txt 0.5 output.txt

def main():

    print "===========================================\n"
    print " +++ Cryptography CT-208 +++ "
    print "- Translate option: " + str(sys.argv[1])
    print "- Input file: " + str(sys.argv[2])
    print "- Key being used: " + str(sys.argv[3])
    print "- Output file: "+ str(sys.argv[4])
    print "-------------------------------------------\n"
    print "===========================================\n"

    

if __name__== "__main__":
    main()
