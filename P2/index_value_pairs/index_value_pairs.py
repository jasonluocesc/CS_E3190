from solution import divide_and_conquer
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python index_value_pairs.py <array file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        # First value in the file is the length of the array
        line = f.readline().split()
        length = int(line[0])
        array = [int(i) for i in line[1:length+1]]

        # Find solution
        ind = divide_and_conquer(array)

        # Output solution
        # Note that the array is treated as having 1-based indexing here
        if ind:
            print("A[%d] = %d" % (ind, ind,))
        else:
            print("No index i for which A[i] = i")
