def sum(a, b):
    """
    >>> sum(5, 7)
    12

    >>> sum(4, -4)
    0
    """
    return a + b


def subtract(a, b):
    """
    >>> subtract(10, 5)
    5
    """
    return a - b



def divide(a, b):
    """
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError('La división por cero no está permitida')
    """
    if b == 0:
        raise ValueError('La división por cero no está permitida')
    return a / b


def multiply(a, b):
    """
    >>> multiply(2, 3)
    6
    """
    return a * b
