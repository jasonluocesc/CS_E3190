# coding: utf-8
def get_longest_path(digraph):
    """Return one longest path in the given digraph, or return None if the graph is cyclic.

    To run doctests:
        python -m doctest -v solution.py
    >>> from networkx import DiGraph
    >>> get_longest_path(DiGraph({1:[2], 2: [1]}))
    >>> get_longest_path(DiGraph({1:[2], 2:[3], 3:[4]}))
    [1, 2, 3, 4]

    Parameters
    ----------
    digraph : DiGraph

    Returns
    -------
    path : list
        List of vertices in the order they appear in the path.
        E.g. if the path is 3 -> 2 -> 1, return [3, 2, 1]. If
        the graph is cyclic, return None.
    """
    # Write your code here.
    g = digraph.copy()                          # the digraph would be changed after topo
    topological_sort = get_topological_sorting(digraph)
    if topological_sort is None:                # check if circle exists
        return None
    ans = max_dis(g)
    return ans


def get_topological_sorting(digraph):
    sinks = set()
    sorted_nodes = []
    for node in digraph.nodes():
        if not digraph.neighbors(node):
            sinks.add(node)
    while len(sinks) > 0:
        sink = sinks.pop()
        sorted_nodes.insert(0, sink)
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
        return sorted_nodes


def max_dis(digraph):
    g = digraph.copy()
    tp = get_topological_sorting(g)
    tp.reverse()
    f = [0] * (len(tp) + 1)
    p = [0] * (len(tp) + 1)

    for i in range(0, len(tp)):
        for node in digraph.predecessors(tp[i]):
            if f[node] < f[tp[i]] + 1:
                f[node] = f[tp[i]] + 1
                p[node] = tp[i]

    index = f.index(max(f))
    count = f[index]
    result = [index]
    while count > 0:
        result.append(p[index])
        index = p[index]
        count = count - 1
    return result


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
