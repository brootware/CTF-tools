#!/usr/bin/env python3
"""
A quick hacky tool created for picoCTF hexadecimal to string conversions
"""

__author__ = "Oaker Min"
__version__ = "0.1.0"
__license__ = "MIT"

import base64


def char2Base64():
    fileWrite = "stringBaseFlag.txt"
    stringInput = input(
        "Key in your base64 to convert. (E.g fsociety  = ZnNvY2lldHk=) : ").strip()

    # Conversion from string to base64
    stringBytes = stringInput.encode('ascii')
    base64Bytes = base64.b64encode(stringBytes)
    base64Message = base64Bytes.decode('ascii')

    with open(fileWrite, "w") as fileWrite:
        fileWrite.write("picoCTF{%s}" % (base64Message) + "\n")
    print("Your base64 converted from strinng is is {}. Look inside your {}".format(
        base64Message, fileWrite))


def main():
    """ Main entry point of the app """
    char2Base64()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
