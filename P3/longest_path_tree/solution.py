# coding: utf-8
def get_longest_path(graph):
    """Return one longest path in the given graph or None, if the graph
    is cyclic.
    
    To run doctests:
        python3 -m doctest -v solution.py
    >>> from networkx import Graph
    >>> get_longest_path(Graph({1: [2], 2: [3], 3: [1]}))
    >>> get_longest_path(Graph({1: [2], 2: [3], 3: [4], 4:[]})) in ([1, 2, 3, 4], [4, 3, 2, 1])
    True

    Parameters
    ----------
    graph : Graph

    Returns
    -------
    path : list or None
        List of vertices in the order they appear in the path.
        E.g. if the path is 3 -> 2 -> 1, return [3, 2, 1]. Return
        None if graph is cyclic.
    """
    
    # Write your code here.
    G=graph
    print(list(dfs_edges(G,1)))
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
