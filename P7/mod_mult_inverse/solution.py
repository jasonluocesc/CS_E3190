# coding: utf-8
def get_multiplicative_inverse(a, p):
    """Find the multiplicative inverse of a (mod p).

    To run doctests:
        python3 -m doctest -v solution.py
    >>> get_multiplicative_inverse(71, 1427)
    201
    >>> get_multiplicative_inverse(1, 2)
    1    
    >>> get_multiplicative_inverse(7, 1012519)
    723228
    >>> get_multiplicative_inverse(805089, 7090328714587)
    2605412154763

    Parameters
    ----------
    a : integer
        in [1, p-1]
    p : integer
        prime

    Returns
    -------
    a_inverse : (long) integer
        1 = a_inverse * a (mod p)
    """
    # Write your code here.
    return 1
