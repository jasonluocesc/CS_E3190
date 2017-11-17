# coding: utf-8
def get_length_of_shortest_cycle(g):
    """Find the length of the shortest cycle in the graph if a cycle exists.

    To run doctests:
        python -m doctest -v solution.py
    >>> from networkx import Graph
    >>> get_length_of_shortest_cycle(Graph({1: [2, 3], 2: [], 3: []})) 
    >>> get_length_of_shortest_cycle(Graph({1: [3], 2: [1], 3: [2]}))
    3
    
    Parameters
    ----------
    g : Graph

    Returns
    -------
    length : int or None
        Length of the shortest cycle, or None if there is no cycle.
    """

    # Write your code here.

    # Hint! If you'd like to test out these commands without
    # writing a full-fledged program, you might want to familiarise
    # yourself with the Python interactive shell or IPython (available
    # on at least some Aalto IT computers)

    # Create a simple line graph g: "(1)->(2)->(3)"
    # (The creation parameter is a dict of {node: list_of_neighbors},
    # but this is not something you will be needing in your code.)
    # >>> from networkx import Graph 
    # >>> g = Graph({1: [2], 2: [3]})
    # >>> g.number_of_nodes()
    # 3

    # Example. Iterate over the nodes and mark them as visited
    # >>> visited = set()
    # >>> for node in g.nodes_iter(): # There is also g.nodes(), which returns a list
    # ...    # do some work here
    # ...    visited.add(node)
    
    # Example. Given a Node v, get all nodes s.t. there is an edge between
    # v and that node
    # >>> g.neighbors(1)
    # [2]

    # Example. Get the edges of the graph:
    # >>> e.edges() # as with nodes, there is also g.edges_iter()
    # [(1, 2), (2, 3)]

    # For more information, consult the NetworkX documentation:
    # https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
    