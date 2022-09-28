#!/usr/bin/python3
"""A class MyList that inherits from list"""

class MyList(list):
    """A class of a list"""
    def print_sorted(self):
        """A function that prints the list, but sorted (ascending sort)"""
		print(sorted(self))
