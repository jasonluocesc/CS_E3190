# coding: utf-8
import sys
from solution import odd_numbers

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: .py <array file>")
        sys.exit(1)
    
    # Read list from given file or stdin
    with open(sys.argv[1]) as f:
        line = f.readline().split()
        number_array = [int(i) for i in line]
        
        # Find solution
        result = odd_numbers(number_array)
        
        # Output solution
        print("The count of odd numbers is %d." % result)
        