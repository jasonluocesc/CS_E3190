# coding: utf-8
def hello_world(n):
    """Prints 'Hello World!' n times to stdout.

    To run doctests:
        python3 -m doctest -v solution.py
    >>> hello_world(3)
    Hello World!
    Hello World!
    Hello World!
    
    Parameters
    ----------

    n : integer
        number of times to repeat 'Hello World!' to stdout

    Returns
    -------
    N/A (no return value)
    """
    
    # Write your code here
    for i in range(0,n):
        print("Hello World!")
    