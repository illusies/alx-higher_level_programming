#!/usr/bin/python3
"""A class BaseGeometry (based on 6-base_geometry.py)"""

class BaseGeometry:
    """A class BaseGeometry"""

    def area(self):
        """A function that raises an Exception with the message area() is not implemented
		"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates value based on:
		PARAMETERS
			self:
			name: string
			value: 	1. If value is not an integer: raise a 
					TypeError exception, with the message <name> must be an integer
					2. if value is less or equal to 0: raise 
					a ValueError exception with the message <name> must be greater than 0
        """
		
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))