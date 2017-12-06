# coding: utf-8
def get_coins(target_value, denominations):
    """Makes change for the given target value using the fewest coins possible.

    To run doctests:
        python3 -m doctest -v solution.py
    >>> get_coins(62, [7, 25, 41])
    [3, 0, 1]
    >>> get_coins(21894, [1506, 1708, 2001, 2009, 2066, 2999, 3003])
    >>> get_coins(60, [1, 2, 5, 10, 20, 50, 100, 200])
    [0, 0, 0, 1, 0, 1, 0, 0]
    >>> get_coins(1, [1, 2, 5])
    [1, 0, 0]

    Parameters
    ----------
    target_value : int
        The amount we need to make change for.
    denominations : list of int, sorted from smallest to largest
        The values of different coins, e.g. [1, 2, 5, 10, 20, 50, 100,
        200] for the euro.

    Returns
    -------
    coins_used : list of int, or None
        A list the same length as denominations, specifying how many of
        each coin were used to get to target_value. Empty or None if we
        cannot form change for target_value using the given
        denominations.
    """
    # Write your code here.
    d_len = len(denominations)
    m = [[1000 for x in range(target_value + 1)] for y in range(d_len)]
    result = [0] * d_len
    for i in range(0, d_len):
        m[i][0] = 0
    for j in range(0, target_value + 1):
        if j % denominations[0] == 0:
            m[0][j] = j // denominations[0]

    for j in range(1, target_value + 1):
        for i in range(0, len(denominations)):
            if j >= denominations[i]:
                m[i][j] = min(m[i - 1][j], 1 + m[i][j - denominations[i]])
            else:
                m[i][j] = m[i - 1][j]

    count = d_len - 1
    heng = target_value
    while count >= 0:
        if m[count][heng] == m[count - 1][heng]:
            if count == 0 and m[count][heng] != 1000:
                result[count] = m[count][heng]
            result[count] = result[count]
            count = count - 1
        else:
            result[count] = result[count] + 1
            heng = heng - denominations[count]
    sum = 0
    for i in range (0,d_len):
        sum = sum + result[i]
    if sum ==0:
        return None
    return result