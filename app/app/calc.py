"""
Calculator functions

"""

def add(x, y):
    """
    Add x and y and return result
    """
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y