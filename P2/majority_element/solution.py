# coding: utf-8
def find_majority_element(data, tiebreaker=None):
    """Return the majority element of the list, if any, or None.
    
    To run doctests:
        python3 -m doctest -v solution.py
    >>> from element import to_element_list
    >>> from majority_element import read_data_from_file
    >>> str(find_majority_element(to_element_list([1, 2])))
    'None'
    >>> str(find_majority_element(read_data_from_file("examples/03.3.instance")))
    '3'

    Parameters
    ----------
    elements : list of Element objects

    Returns
    -------
    element : Element or None
        One of the majority elements in the lists (if exists), otherwise None
        E.g. if no majority element, return None.
    """
    
    # Write your code here.
    length = len(data)

    if length == 0:
        return tiebreaker

    pairs = []

    if length % 2 == 1:
        tiebreaker = data[-1]

    for i in range(0, length - 1, 2):
        if data[i] == data[i + 1]:
            pairs.append(data[i])

    major = find_majority_element(pairs, tiebreaker)

    if major is None:
        return None
    majorTime = data.count(major)
    
    if 2 * majorTime > length or (2 * majorTime == length and major == tiebreaker):
        return major
    return None
