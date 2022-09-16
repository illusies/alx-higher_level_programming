#!/usr/bin/python3
""" A class Square that defines a square by: (based on 4-square.py)"""

class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """
        PARAMETERS
        size:
            1. must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            2. if size is less than 0, raise a ValueError exception with the message size must be >= 0
        """
        
        self.size = size

    @property
    def size(self):
        """Function that get the current size of the square."""
        
        return (self.__size)

    @size.setter
    def size(self, value):
        """Function that set the current size of the square."""
        
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function that returns the current area of the square."""
        
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Function that defines the == comparision to a Square."""
        
        return self.area() == other.area()

    def __ne__(self, other):
        """Function that defines the != comparision to a Square."""
        
        return self.area() != other.area()

    def __lt__(self, other):
        """Function that defines the < comparision to a Square."""
        
        return self.area() < other.area()

    def __le__(self, other):
        """Function that defines the <= comparision to a Square."""
        
        return self.area() <= other.area()

    def __gt__(self, other):
        """Function that defines the > comparision to a Square."""
        
        return self.area() > other.area()

    def __ge__(self, other):
        """Function that defines the >= comparision to a Square."""
        
        return self.area() >= other.area()
