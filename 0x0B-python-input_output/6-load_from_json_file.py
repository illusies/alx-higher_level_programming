#!/usr/bin/python3
'''A function that creates an Object from a “JSON file”'''

from json import JSONDecoder

def load_from_json_file(filename):
    '''A function that creates an Object from a “JSON file”
    PARAMETER
        filename:
    '''
    
    lines = []
    with open(filename, encoding='utf-8') as file:
        for line in file.readlines():
            lines.append(line)
    return JSONDecoder().decode(''.join(lines))
