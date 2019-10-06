'''
Extmod: Cool stuff in here!!!
'''

def root(anum, rootnum):
    '''
    root: Get the root of a number. Can be any root. Square,
    Cube, etc.

    Params: anum - the number to root
            rootnum - whatever

    Usage
    >>> root(4,2)
    2.0

    >>> root(8,3)
    2.0

    >>> root(25,5)
    1.9036539387158786

    >>> root(25,-5)
    0
    
    '''
    if rootnum <= 0:
        return 0
    else:
        ans = anum ** (1 / rootnum)
        return ans

def summ(anum):
    '''
    Summ: do a summation thing.

    >>> summ(5)
    15

    >>> summ(3)
    6

    >>> summ(-3)
    0

    '''
    s = 0
    for n in range(1, anum + 1):
        s += n
    
    return s

# print("extmod:", __name__)
if __name__ == "__main__":
    # RUN UNIT TESTS
    import doctest
    doctest.testmod()
