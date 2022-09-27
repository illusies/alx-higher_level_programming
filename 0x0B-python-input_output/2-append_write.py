#!/usr/bin/python3
'''A function that appends a string at the end of a text file (UTF8) and returns the number of characters added
'''

def append_write(filename="", text=""):
    '''A function that appends a string at the end of a text file (UTF8) and returns the number of characters added
    PARAMETERS
        filename:
        text:
    '''
    
    n = 0
    with open(filename, mode='a', encoding='utf-8') as file:
        n = file.write(text)
    return n
