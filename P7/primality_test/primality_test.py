import sys
from modelsolution import is_prime

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 is_prime.py <int>")
    N = int(sys.argv[1])
    result = is_prime(N)
    if result:
        print("Prime.")
    else: 
        print("Not prime.")