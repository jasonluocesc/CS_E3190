# coding: utf-8

from solution import find_optimal_locations
import sys

def read_data_from_file(filename):
    """Read problem instance from file. No error handling!

    Parameters
    ----------
    filename : str
    
    Returns
    -------
    num_locations : int
        Number of locations
    min_distance : int
        Minimum distance between two stations in miles.
    distances : list of int
        Distance from the start of the highway to each location available.
    profits : list of int
        Amount of profit we would get from a station at this location.
    """
    with open(filename) as f:
        min_distance, num_locations = [int(value) for value in f.readline().split()]
        distances = [int(value) for value in f.readline().split()]
        profits = [int(value) for value in f.readline().split()]
        return (num_locations, min_distance, distances, profits)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: fuel_stations.py <input_file>")
        sys.exit(1)

    (num_locations, min_distance, distances, profits) = read_data_from_file(sys.argv[1])

    (P, stations) = find_optimal_locations(min_distance, distances, profits)
    
    print("Profit: %d" % P)
    print("Locations used: %s" % (" ".join([str(value) for value in stations])))

