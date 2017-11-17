# coding: utf-8
def get_coefficient(a, b, p):
    """Finds a coefficient c such that a is congruent to b * c (mod p).

    To run doctests:
        python3 -m doctest -v solution.py
    >>> get_coefficient(130, 54, 137)
    43
    >>> get_coefficient(125, 145, 1301)
    1257
    >>> get_coefficient(288, 4085, 9851)
    656

    Parameters
    ----------
    a : integer
        in [0, p-1]
    b : integer
        in [1, p-1]
    p : integer
        prime

    Returns
    -------
    c : integer
        in [0, p-1]
    """
    # Write your code here. You should be calling the function
    # extended_euclid() from this function.
    return 0


def extended_euclid(val1, val2):
    # Write your code for the extended Euclidean algorithm here.
    # You may freely choose what values this function returns.
    pass

