#!/usr/bin/python3

''' 
    Divides all elements of a matrix by a given divisor.
    All elements of the matrix are divided by div,
    rounded to 2 decimal places.
'''
def matrix_divided(matrix, div):
    ''' 
        Args:
        - matrix (list of lists): The input matrix to be divided.
        - div (int or float): The divisor used for division.
        Returns:
        - list of lists: A new matrix where each element is the result of the division rounded to 2 decimal places.
        Raises:
        - TypeError: If `div` is not a number, if the matrix is not a list of lists, or if the elements in the matrix are not numbers.
        - ZeroDivisionError: If `div` is 0.
        - TypeError: If the rows in the matrix have different sizes.
    '''
    if not isinstance(div,(int,float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    if isinstance(matrix, list) and len(matrix) > 0 and all(isinstance(row, list) and all(isinstance(el,(int,float)) for el in row) for row in matrix):
        el_length = len(matrix[0])
        if not all(len(row) == el_length for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])