# coding: utf-8
import sys
from solution import fizzbuzz

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: .py <int> <int>")
        sys.exit(1)
    
    
    begin = int(sys.argv[1])
    end = int(sys.argv[2])
    # Call the function
    fizzbuzz(begin, end)
