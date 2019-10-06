def sqrt(anum):
    '''
    sqrt:
    This gives you a square root.

    Usage:
    >>> print(sqrt(16))
    4.0

    >>> print(sqrt(1))
    1.0

    >>> print(sqrt(-4))
    (1.2246467991473532e-16+2j)

    '''
    # print("sqrt:", __name__)
    return anum ** 0.5

def summ(anum):
    '''
    sqrt:
    This gives you a square root.

    Usage:
    >>> summ(5)
    15

    >>> summ(4)
    10

    >>> summ(-4)
    0
    
    >>> summ(500000)
    125000250000
    
    '''
    s = 0
    for n in range(1, anum + 1):
        s += n
    return s

if __name__ == "__main__":
    # RUN UNIT TESTS
    import doctest
    doctest.testmod()

