def get_bipartition(g):
    """For a bipartite graph, returns a list of nodes S s.t. (S, V\S) is a bipartition.

    >>> from networkx import Graph
    >>> get_bipartition(Graph({1: [2, 3], 2: [], 3: []})) in ([1], [2, 3])
    True

    Parameters
    ----------
    g : Graph

    Returns
    -------
    partition : list
        List of all nodes on one side of the partition. None if the
        graph is not bipartite.
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
    