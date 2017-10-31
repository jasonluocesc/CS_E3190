from solution import get_nth_smallest_value
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nth_smallest.py <array file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        # 1st element is the length of both arrays
        line = f.readline().split()
        length = int(line[0])
        array1 = [int(i) for i in line[1:length+1]]
        array2 = [int(i) for i in line[length+1:length*2+1]]

        # Find solution
        elem = get_nth_smallest_value(array1, array2)

        # Output solution
        print("The nth smallest element is %d" % (elem,))

