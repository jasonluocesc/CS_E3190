# coding: utf-8
def get_topological_sorting(digraph):


    """Given a directed graph, returns a list of nodes in topological order.

    To run doctests:
        python -m doctest -v solution.py
    >>> from networkx import DiGraph
    >>> get_topological_sorting(DiGraph({1: [], 2: [1], 3: [2]}))
    [3, 2, 1]
    >>> get_topological_sorting(DiGraph({1: [3], 2: [1], 3: [2]}))

    Parameters
    ----------
    digraph : DiGraph, a graph container instance

    Returns
    -------
    sorting : list of integers corresponding to node indices in the graph
        None, if there is no topological sorting (i.e., the graph is
        cyclic.
    """

    # Write your code here.
    sinks = set()
    sortedNode = []

    for node in digraph.nodes():
        if not digraph.neighbors(node):
            sinks.add(node)

    while len(sinks) > 0:
        sink = sinks.pop()
        sortedNode.insert(0, sink)
        pres = []

        for pre in digraph.predecessors(sink):
            pres.append(pre)

        for node in pres:
            digraph.remove_edge(node, sink)
            if not digraph.neighbors(node):
                sinks.add(node)

    if digraph.edges():
        return None
    else:
        return sortedNode

    # Hint! If you'd like to test out these commands without
    # writing a full-fledged program, you might want to familiarise
    # yourself with the Python interactive shell or IPython (available
    # on at least some Aalto IT computers)

    # Create a simple line digraph g: "(1)->(2)->(3)"
    # (The creation parameter is a dict of {node: list_of_successors},
    # but this is not something you will be needing in your code.)
    # >>> from networkx import DiGraph 
    # >>> g = DiGraph({1: [2], 2: [3]})
    # >>> g.number_of_nodes()
    # 3

    # Example. Iterate over the nodes and mark them as visited
    # >>> visited = set()
    # >>> for node in g.nodes_iter(): # There is also g.nodes(), which returns a list
    # ...    if node not in visited:
    # ...       # do some work here
    # ...       visited.add(node)
    
    # Example. Given a Node v, get all nodes s.t. there is an arc from
    # v to that node
    # >>> g.neighbors(1)
    # [2]

    # Example. Given a Node v, get all nodes s.t. there is an arc from
    # that node to v
    # >>> g.predecessors(2)
    # [1]

    # Example. Get the edges of the graph:
    # >>> e.edges() # as with nodes, there is also g.edges_iter()
    # [(1, 2), (2, 3)]
    
    # For more information, consult the NetworkX documentation:
    # https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
