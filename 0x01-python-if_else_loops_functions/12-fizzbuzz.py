#!/usr/bin/python3

def fizzbuzz():
    """Print out numbers from 1 to 100"""

    for number in range(1, 101):

        if number % 3 == 0 and number % 5 != 0:

            print("Fizz ", end="")

        elif number % 5 == 0 and number % 3 != 0:

            print("Buzz ", end="")

        elif number % 15 == 0:

            print("FizzBuzz ", end="")

        else:

            print("{:d} ".format(number), end="")
