# coding: utf-8
from solution import get_coefficient
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            a, b, prime = (int(x) for x in f.readline().split())
    elif len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        prime = int(sys.argv[3])
    else: 
        print("Usage: python mod_division.py <int> <int> <prime> OR python mod_division.py <filename>")
        sys.exit(1)

    # Find solution
    c = get_coefficient(a, b, prime)

    # Output solution
    #print(u"%d \u2261 %d * %d (mod %d)" % (a, b, c, prime))
    print("%d = %d * %d (mod %d)" % (a, b, c, prime))
