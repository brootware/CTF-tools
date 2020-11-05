#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Oaker Min - https://github.com/Brucius"
__version__ = "0.1.0"
__license__ = "MIT"

def caesarEncrypt(uInput):
    result = ''
    for i in range(len(uInput)): # go through each character of the uInput using this loop
        char_pos = ord(uInput[i]) # obtain ascii value using ord
        char_pos = char_pos - 97 # subtract 97 (127-97=26 refer to ascii table) to have a chracter from 1 to 26
        new_char_pos = char_pos + 3 # add 3 to the position as caesar does
        new_char_pos = new_char_pos % 26 # make sure the position does not surpass 26 (it wraps around instead)
        new_char_pos = new_char_pos + 97 # add 97 back to be converted back to ascii values
        result = result + chr(new_char_pos)
        print(result)
    return result




def caesarDecrypt(dInput):
    """
    docstring
    """
    pass



def main():
    """ Main entry point of the app """
    uInput = input("Key in your message to encrypt using caesar cipher : ")
    caesarEncrypt(uInput)

    dInput = input("Key in your message decrypt caesar cipher : ")
    caesarEncrypt(dInput)




if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()