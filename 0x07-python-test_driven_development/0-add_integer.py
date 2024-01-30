#!/usr/bin/python3

'''
    Defines a two integer addition function.
    The second argument is 98 by default.
    Float arguments are typecasted to ints
    before addition is performed.
'''
def add_integer(a, b=98):
    '''
        Returns the addition of the first and second argument,
        Raises TypeError if one of the arguments is not and integer or float.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
