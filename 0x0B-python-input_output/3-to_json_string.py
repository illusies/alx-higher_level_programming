#!/usr/bin/python3
'''A function that returns the JSON representation of an object (string)'''

from json import JSONEncoder

def to_json_string(my_obj):
    '''A function that returns the JSON representation of an object (string)
    PARAMETERS
        my_obj: 
    '''
    
    return JSONEncoder().encode(my_obj)
