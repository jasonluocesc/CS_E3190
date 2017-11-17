from solution import pretty_print
import sys


def line_cost(line, max_line_length):
    words = line.split()
    line_length = sum(len(word) for word in words) + len(words) - 1
    return max_line_length - line_length


def total_cost(text, max_line_length):
    lines = text.split("\n")
    return sum(line_cost(line, max_line_length) for line in lines)


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage: python pretty_printing.py <file>")
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        max_line_length = int(f.readline())
        text = f.read()

    pretty = pretty_print(text, max_line_length)
    
    for line in pretty.split("\n"):
        #if len(line) < max_line_length:
        #    line += "*" * (max_line_length - len(line))
        print(line)
    print("Cost: %d" % total_cost(pretty, max_line_length))