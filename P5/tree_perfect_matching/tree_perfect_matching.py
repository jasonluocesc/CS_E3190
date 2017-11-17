# coding: utf-8

from networkx import Graph
from solution import tree_perfect_matching
import sys

def read_graph_in_dimacs_format(filename):
    with open(filename) as f:
        line = f.readline()
        while line.startswith('c '):
            line = f.readline()
        tokens = line.split()
        num_nodes = int(tokens[2])
        num_edges = int(tokens[3])
        G = Graph()
        G.add_nodes_from(range(1, num_nodes+1))
        for i in range(num_edges):
            tokens = f.readline().split()
            n1 = int(tokens[1])
            n2 = int(tokens[2])
            G.add_edge(n1, n2)
        return G

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tree_perfect_matching.py <file>")
        sys.exit(1)

    # Read graph from given file
    g = read_graph_in_dimacs_format(sys.argv[1])

    # Get matching
    matching = tree_perfect_matching(g)

    # Output the result
    if matching is None:
        print("No perfect matching.")
    else:
        print(" ".join("({},{})".format(edge[0], edge[1]) for edge in matching))