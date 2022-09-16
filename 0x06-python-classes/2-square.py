#!/usr/bin/python3
""" A class Square that defines a square by: (based on 1-square.py)"""

class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """
        PARAMETERS
        size:
            1. must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            2. if size is less than 0, raise a ValueError exception with the message size must be >= 0
        """
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
