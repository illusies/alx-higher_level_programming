#!/usr/bin/python3
""" A class Square that defines a square by: (based on 5-square.py)"""

class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0,0)):
        """
        PARAMETERS
        size:
            1. must be an integer, otherwise raise a TypeError exception with the message size must be an integer
            2. if size is less than 0, raise a ValueError exception with the message size must be >= 0
        position: 
            A tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
        """
        
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Function that get the current position of the square."""
        
        return (self.__position)

    @position.setter
    def position(self, value):
        """Function that set the current position of the square."""
        
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Function that returns the current square area"""
        
        return (self.__size * self.__size)

    def my_print(self):
        """Function that prints in stdout the square with the character #"""
        
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
