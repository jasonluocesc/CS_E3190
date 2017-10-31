from element import Element
from solution import find_majority_element
import sys


def read_data_from_file(filename):
    """Read problem instance from file. No error handling!

    Parameters
    ----------
    filename : str
    
    Returns
    -------
    elements : list of Elements in the order they exist in the file
    """
    with open(filename) as f:
        elements = [Element(int(value)) for value in f.readline().split()]
        return elements

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: .py <file>")
        sys.exit(1)
        
    # Read elements from given file or stdin
    elements = read_data_from_file(sys.argv[1])

    # Find majority element of longest path if one exists
    answer = find_majority_element(elements)
    
    # Output the result
    if answer:
        if isinstance(answer, int):
            print("Note! you are supposed to return the object element.")
        print(str(answer))
    else:
        print("No majority element")
