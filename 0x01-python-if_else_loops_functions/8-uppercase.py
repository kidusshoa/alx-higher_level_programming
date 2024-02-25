#!/usr/bin/python3

def uppercase(str):
    """Prints uppercase string

    Args:
        str: a character string argument
    """

    for letter in str:

        ascii_letter_code = ord(letter)

        if ascii_letter_code in range(97, 123):

            ascii_letter_code = ascii_letter_code - 32

        print("{:c}".format(ascii_letter_code), end="")
    print()
