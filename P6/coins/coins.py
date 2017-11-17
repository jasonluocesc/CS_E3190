# coding: utf-8

from solution import get_coins
import sys

def read_data_from_file(filename):
    """Read problem instance from file. No error handling!

    Parameters
    ----------
    filename : str
    
    Returns
    -------
    target_value : int
        The amount we need to make change for using the different denominations.
    denominations : list of int, sorted from smallest to largest
        The values of different coins, e.g. [1, 2, 5, 10, 20, 50, 100, 200] for the euro.
    """
    with open(filename) as f:
        target_value, num_denominations = [int(value) for value in f.readline().split()]
        denominations = [int(value) for value in f.readline().split()]
        return (target_value, denominations)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: coins.py <input_file>")
        sys.exit(1)

    (target_value, denominations) = read_data_from_file(sys.argv[1])

    coins_used = get_coins(target_value, denominations[:])

    if coins_used:
        print("%(target_value)d = %(maths)s" %
            {'target_value': target_value,
            'maths': " + ".join("%d * %d" % (coins_used[i], denominations[i]) for i in range(len(denominations)) if coins_used[i])})
    else:
        print("Cannot form change of %d." % target_value)
