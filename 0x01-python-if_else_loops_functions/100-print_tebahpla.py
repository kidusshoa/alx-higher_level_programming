#!/usr/bin/python3

for ascii_code in range(122, 96, -1):

    if ascii_code % 2 == 1:

        ascii_code = ascii_code - 32

    print("{:c}".format(ascii_code), end="")
