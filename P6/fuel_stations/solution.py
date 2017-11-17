# coding: utf-8
def find_optimal_locations(min_distance, distances, profits):
    """Find the globally optimal solutions 'at each location'.
    
    To run doctests:
        python3 -m doctest -v solution.py
    >>> find_optimal_locations(4, [3, 4, 7, 10], [56, 37, 68, 49])
    (124, [0, 2])
    >>> find_optimal_locations(5, [2, 6, 8, 11, 13],
    ... [5434, 5915, 4720, 5601, 3866])
    (14020, [0, 2, 4])

    Parameters
    ----------
    min_distance : int
        Minimum distance between two chosen locations in miles.
    distances : list of int
        The distance to each location from the start of the highway.
        The distances to the locations are at distances[0]...distances[num_locations-1]
    profits : list of int
        The amount of profit we would get if we were to build a station
        at this location.

    Returns
    -------
    profit : int
        Profit from the optimal selection of locations.
    stations : list of int, corresponding to the indices of the stations used in the optimal solution
    """
    # Write your code here.
