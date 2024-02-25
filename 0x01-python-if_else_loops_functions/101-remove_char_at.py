#!/usr/bin/python3

def remove_char_at(str, n):
    """Removes the char at an index in a given string

    Args:
        str: string argument
        n: index argument

    Returns:
        str: edited string
    """

    if n >= 0:

        str = str[:n] + str[n + 1:]

    return str
