#!/usr/bin/python3
"""A function that adds a new attribute to an object if it’s possible"""

def add_attribute(obj, att, value):
    """A function that adds a new attribute to an object if it’s possible
    PARAMETERS:
		obj: object
		att: attribute
		value: value
    """
	
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
