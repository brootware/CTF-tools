#!/usr/bin/env python3
"""
A quick hacky tool created for picoCTF base64 to string conversions
"""

__author__ = "Oaker Min"
__version__ = "0.1.0"
__license__ = "MIT"

import base64


def base642String():
    fileWrite = "base64StringFlag.txt"
    base64Char = input(
        "\n Key in your base64 to convert. (E.g ZnNvY2lldHk= = fsociety) : ").strip()

    # Conversion from base64 to char
    base64Bytes = base64Char.encode('ascii')
    stringBytes = base64.b64decode(base64Bytes)
    message = stringBytes.decode('ascii')

    with open(fileWrite, "w") as fileWrite:
        fileWrite.write("picoCTF{%s}" % (message) + "\n")
    print("\n Your string converted from base64 is {}. Look inside your {}".format(
        message, fileWrite))


def hex2String():
    fileWrite = "hexStringFlag.txt"
    base16Char = input(
        "\n Key in your hex number to convert. (E.g 41 = A) : ").strip()

    message = bytearray.fromhex(base16Char).decode()

    with open(fileWrite, "w") as fileWrite:
        fileWrite.write("picoCTF{%s}" % (message) + "\n")
    print("\n Your ascii character converted from hex is {}. Look inside your {}".format(
        message, fileWrite))


def menu():
    return int(input(
        "\n Choose type of base to decode from (16,32,64) \n\n 1) Base64 decoder \n 2) Hexadecimal decoder \n 3) Base32 decoder \n 4) Quit \n\n Your Choice : "))


def main():
    """ Main entry point of the app """
    stringTable = {

    }

    while True:
        choice = menu()
        if choice == 1:
            base642String()
        elif choice == 2:
            hex2String()
        elif choice == 3:
            print("\nHaven't finished this function yet")
        elif choice == 4:
            print("\n Goodbye!")
            break

    # fileWrite = "picoFlag.txt"
    # decodeInput = input(
    #     "Key in your encoded string to convert. (E.g base64 conversion ZnNvY2lldHk= = fsociety) : ").strip()

    # stringTable = {
    #     "b64String": base642String(decodeInput),
    #     "b16String": hex2String(decodeInput)
    # }
    # # b64String = base642String(decodeInput)
    # # b16String = hex2String(decodeInput)

    # with open(fileWrite, "w") as fileWrite:
    #     for key, value in stringTable.items():
    #         fileWrite.write("{} = picoCTF{{{}}}".format(key, value) + "\n")
    # #     fileWrite.write("picoCTF{%s}" % (b64String) + "\n")
    # print("Your strings have been converted. Look inside your {}".format(fileWrite))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
