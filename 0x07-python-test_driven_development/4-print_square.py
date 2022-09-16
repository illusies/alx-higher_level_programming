#!/usr/bin/python3
"""A function that prints a square with the character #."""

def print_square(size):
    """
    1. size is the size length of the square
    2. size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    3. if size is less than 0, raise a ValueError exception with the message size must be >= 0
    4. if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
    5. You are not allowed to import any module
    """
    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
