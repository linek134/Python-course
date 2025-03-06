"""
A collection of simple math operations
"""


def simple_add(a,b):
    """Function generating the sum of two numerical values.
    """
    return a+b

def simple_sub(a,b):
    """Function generating the difference between two numerical values.
    """ 
    return a-b

def simple_mult(a,b):
    """Function generating the product of two numerical values.
    """ 
    return a*b

def simple_div(a,b):
    """Function generating the the quotient of two numerical values
    """
    return a/b

def poly_first(x, a0, a1):
    """Function calculating the result of a first-degree polynomial equation.
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Function calculating the result of a second-degree polynomial equation.
    """
    return poly_first(x, a0, a1) + a2*(x**2)
