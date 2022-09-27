#!/usr/bin/python3
"""A class MyInt that inherits from int"""

class MyInt(int):
    """A class that inverts operators == and !="""

    def __eq__(self, value):
        """A function that overrides the == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """A function that overrides the =! operator with == behavior."""
        return self.real == value
