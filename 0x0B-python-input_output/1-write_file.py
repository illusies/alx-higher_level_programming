#!/usr/bin/python3
'''A function that writes a string to a text file (UTF8) and returns the number of characters written'''

def write_file(filename="", text=""):
    '''A function that writes a string to a text file (UTF8) and returns the number of characters written
    PARAMETERS
        filename:
        text:
    '''
    
    n = 0
    with open(filename, mode='w', encoding='utf-8') as file:
        n = file.write(text)
    return n
