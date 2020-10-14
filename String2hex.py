#!/usr/bin/env python3
"""
A quick hacky tool created for picoCTF string to hex conversions
"""

__author__ = "Oaker Min"
__version__ = "0.1.0"
__license__ = "MIT"

import binascii
from binascii import hexlify


def Char2hex():
    fileWrite = "hexflag.txt"
    # hexInput = input("Key in your ascii character. (E.g 41 = A) : ")

    charInput = str(
        input("Key in your string to convert to hex. (E.g A = 41) : ")).strip()

    charInput = hexlify(charInput.encode())
    charInput = charInput.decode()

    with open(fileWrite, "w") as fileWrite:
        fileWrite.write("picoCTF{%s}" % (charInput) + "\n")

    print("Your hexadecimal number converted from string is {}. Look inside your {}".format(
        charInput, fileWrite))


def main():
    """ Main entry point of the app """
    Char2hex()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
