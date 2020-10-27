#!/usr/bin/env python3
"""
A quick hacky tool for common variant of caesar cipher that replaces letters with numbers.
"""

__author__ = "Oaker Min - https://github.com/Brucius"
__version__ = "0.1.0"
__license__ = "MIT"


def num2Letters():
    fileWrite = "numFlag.txt"
    numList = []

    for i in range(26):
        numList.append(chr(ord("A") + i))
        print(numList)

    
    # numInput = input(
    #     "Key in your letters to be converted to alphabets seperated by space : ").split(' , ')

    # for i in numInput:
    #     ele = int(input())
    #     numList.append(ele)
    #     print(numList)
    # Conversion from hex to char
    # numInput = chr(numInput)

    # with open(fileWrite, "w") as fileWrite:
    #     fileWrite.write("picoCTF{%s}" % (numInput) + "\n")
    # print("Your ascii character converted from hex is {}. Look inside your {}".format(
    #     numInput, fileWrite))
# 16, 9, 3, 15, 3, 20, 6

def main():
    """ Main entry point of the app """
    num2Letters()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()