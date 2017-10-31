# coding: utf-8
def divide_and_conquer(A):
    """Finds i such that the i-th element in the list has value i, or returns None.

    To run doctests:
        python3 -m doctest -v solution.py
    >>> divide_and_conquer([2, 3, 4])
    >>> divide_and_conquer([-1, 2, 4])
    2
    >>> divide_and_conquer([-8, -7, -4, -3, -1, 2, 5, 7, 9, 11, 14, 16, 19, 22, 25])
    9

    Parameters
    ----------
    A : list of int
        Sorted. Note that the element at index 0 is considered the 1st
        element, the one at index 1 is the 2nd, and so on.

    Returns
    -------
    index : int or None
        index s.t. A[i-1] = i, or None if no such index exists.
    """
    # Write your code here.
    # Your code should execute in time O(log n).
    return None
