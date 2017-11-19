# coding: utf-8
import sys
from solution import hello_world

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: .py <int>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    
    # Call the function
    hello_world(n)
