# coding: utf-8

from networkx import DiGraph
from solution import get_topological_sorting
import sys

def read_digraph_in_dimacs_format(filename):
    with open(filename) as f:
        line = f.readline()
        while line.startswith('c '):
            line = f.readline()
        tokens = line.split()
        num_nodes = int(tokens[2])
        num_edges = int(tokens[3])
        G = DiGraph()
        G.add_nodes_from(range(1, num_nodes+1))
        for i in range(num_edges):
            tokens = f.readline().split()
            n1 = int(tokens[1])
            n2 = int(tokens[2])
            G.add_edge(n1, n2)
        return G


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python topological_sorting.py <file>")
        sys.exit(1)

    # Read graph from given file
    digraph = read_digraph_in_dimacs_format(sys.argv[1])

    # Get topological sorting
    sorting = get_topological_sorting(digraph)

    # Output the result
    if sorting:
        print(" ".join(str(node) for node in sorting))
    else:
        print("cyclic")
