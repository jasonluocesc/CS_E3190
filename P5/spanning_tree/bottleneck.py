# coding: utf-8

from networkx import Graph
from solution import get_spanning_tree
import sys

def read_weighted_graph_in_dimacs_format(filename):
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
            w = int(tokens[3])
            G.add_edge(n1, n2, weight=w)
        return G

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python minimal_vertex_cover.py <file>")
        sys.exit(1)

    # Read weighted graph from given file
    g = read_weighted_graph_in_dimacs_format(sys.argv[1])

    # Get spanning_tree
    bottleneck, tree_edges = get_spanning_tree(g)

    # Output the result
    for edge in tree_edges:
        print("%3d %3d %3d" % (edge[0], edge[1], g[edge[0]][edge[1]]['weight']))
    print("bottleneck: %d" % bottleneck)
