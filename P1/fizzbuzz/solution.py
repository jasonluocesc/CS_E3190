# coding: utf-8
def fizzbuzz(begin, end):
    """Prints 'Fizz' to stdout if the current number is divisible by 3
    and 'Buzz' if it is divisible by 5. If the number is divisible by
    both 3 and 5, the function will then print 'Fizz Buzz' to stdout.
    If aforementioned rules are not applicable, the function will
    simply just print the current number to stdout.
    
    The numbers are to be processed incrementally, starting from
    the integer value of the first parameter and including the
    integer value of the second parameter.

    To run doctests:
        python3 -m doctest -v solution.py
    >>> fizzbuzz(1, 6)
    1
    2
    Fizz
    4
    Buzz
    Fizz
    
    Parameters
    ----------

    begin : integer
        the first number to be processed by the function
    end : integer
        the last number to be processed by the function

    Returns
    -------
    N/A (no return value)
    """
    
    # Write your code here
    for i in range(begin, end+1):

        if i%15 == 0:
            print("Fizz Buzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 ==0:
            print("Fizz")
        else:
            print(i)
