#!/usr/bin/python3

def print_last_digit(number):
    """Prints last digit of number

    Args:
        number: a number

    Returns:
        last_digit: the value of the last digit
    """

    last_digit = int(repr(number)[-1])

    print("{}".format(last_digit), end="")
    return last_digit
