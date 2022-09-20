#!/usr/bin/python3
"""A task to write unittests for the function def max_integer(list=[]):"""

def max_integer(list=[]):
    """
    1. Your test file should be inside a folder tests
    2. You have to use the unittest module
    3. Your test file should be python files (extension: .py)
    4. Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
    """
    
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
