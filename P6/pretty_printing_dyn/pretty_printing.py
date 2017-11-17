from solution import pretty_print
import sys

def line_cost(line, max_line_length):
    words = line.split()
    line_length = sum(len(word) for word in words) + len(words) - 1
    return (max_line_length - line_length) ** 2

def total_cost(text, max_line_length):
    if len(text) == 0:
        return 0
    lines = text.split("\n")
    return sum(line_cost(line, max_line_length) for line in lines) - line_cost(lines[-1], max_line_length)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pretty_printing.py <file>")
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        max_line_length = int(f.readline())
        text = f.read()

    pretty = pretty_print(text, max_line_length)
    
    print(pretty)
    print("Cost: %d" % total_cost(pretty, max_line_length))