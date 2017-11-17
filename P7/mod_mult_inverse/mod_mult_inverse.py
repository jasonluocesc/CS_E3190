# coding: utf-8
from solution import get_multiplicative_inverse
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            a, prime = (int(x) for x in f.readline().split())
    elif len(sys.argv) == 3:
        a = int(sys.argv[1])
        prime = int(sys.argv[2])
    
    else:
        print("Usage: python mod_mult_inverse.py <int> <prime> OR python mod_mult_inverse.py <filename>")
        sys.exit(1)


    a_inverse = get_multiplicative_inverse(a, prime)

    print("1 = %d * %d (mod %d)" % (a, a_inverse, prime))
