#!/usr/bin/python3
"""A function that inserts a line of text to a file, after each line containing a specific string (see example)
"""

def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file, after each line containing a specific string (see example)
    PARAMETER
        filename:
        search_string:
        new_string:
    """
    
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
