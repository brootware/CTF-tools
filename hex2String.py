#!/usr/bin/env python3
"""
A quick hacky tool created for picoCTF hexadecimal to string conversions
"""

__author__ = "Oaker Min"
__version__ = "0.1.0"
__license__ = "MIT"


def hex2Char():
    fileWrite = "stringFlag.txt"
    hexInput = input(
        "Key in your hex number to convert. (E.g 41 = A) : ").strip()

    # Conversion from hex to char
    hexInput = bytearray.fromhex(hexInput).decode()

    with open(fileWrite, "w") as fileWrite:
        fileWrite.write("picoCTF{%s}" % (hexInput) + "\n")
    print("Your ascii character converted from hex is {}. Look inside your {}".format(
        hexInput, fileWrite))


def main():
    """ Main entry point of the app """
    hex2Char()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
