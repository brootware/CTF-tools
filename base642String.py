#!/usr/bin/env python3
"""
A quick hacky tool created for picoCTF hexadecimal to string conversions
"""

__author__ = "Oaker Min"
__version__ = "0.1.0"
__license__ = "MIT"

import base64


def base642String():
    fileWrite = "baseStringFlag.txt"
    baseInput = input(
        "Key in your base64 to convert. (E.g ZnNvY2lldHk= = fsociety) : ").strip()

    # Conversion from base64 to char
    base64Bytes = baseInput.encode('ascii')
    stringBytes = base64.b64decode(base64Bytes)
    message = stringBytes.decode('ascii')

    with open(fileWrite, "w") as fileWrite:
        fileWrite.write("picoCTF{%s}" % (message) + "\n")
    print("Your string converted from base64 is {}. Look inside your {}".format(
        message, fileWrite))


def main():
    """ Main entry point of the app """
    base642String()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
