#!/usr/bin/python3
""" A functon that divides all elements of a matrix """

def matrix_divided(matrix, div):
    """
    1. matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
    2. Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
    3. div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
    4. div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
    5. All elements of the matrix should be divided by div, rounded to 2 decimal places
    6. Returns a new matrix
    7. You are not allowed to import any module
    """
    
    messages = (
        'matrix must be a matrix (list of lists) of integers/floats',
        'Each row of the matrix must have the same size',
        'div must be a number',
        'division by zero'
    )
    size = [0, 0]
    res = []
    if not isinstance(matrix, list):
        raise TypeError(messages[0])
    size[0] = len(matrix)
    if size[0] == 0:
        raise TypeError(messages[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(messages[0])
        elif len(row) == 0:
            raise TypeError(messages[0])
        else:
            if size[1] == 0:
                size[1] = len(row)
            elif len(row) != size[1]:
                raise TypeError(messages[1])
            for col in row:
                if not isinstance(col, (int, float)):
                    raise TypeError(messages[0])
    if not isinstance(div, (int, float)):
        raise TypeError(messages[2])
    elif div == 0:
        raise ZeroDivisionError(messages[3])
    else:
        for row in matrix:
            res_row = list(map(lambda x: round(x / div, 2), row))
            res.append(res_row)
        return res
