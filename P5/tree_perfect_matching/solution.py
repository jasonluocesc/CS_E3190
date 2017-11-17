def tree_perfect_matching(tree):
    """For a tree, return a list of edges that constitutes a perfect matching: a set of edges having no endpoints in common that covers all vertices.
    
    To run doctests:
        python -m doctest -v solution.py
    >>> from networkx import Graph
    >>> tree_perfect_matching(Graph({1: [2, 3], 2: [], 3: []}))
    >>> sorted(tree_perfect_matching(Graph({1: [3], 2: [4], 3: [2]}))) in ([(1, 3), (2, 4)], [(2, 4), (3, 1)], [(1, 3), (4, 2)], [(3, 1), (4, 2)])
    True
    >>>
    tree_perfect_matching()
    
    Parameters
    ----------
    tree : Graph

    Returns
    -------
    matching : list
        list of edges (as (int, int) tuples) that constitutes a perfect matching, or None.
    """
    
    # Write your code here
    if len(tree.adj) == 0:
        return []
    result = []
    visited = set()
    new_tree = tree.copy()
    while len(new_tree.edges()) > 0:
        for node in tree.adj:
            if node in visited:
                continue
            elif len(new_tree.adj[node]) == 1:
                new_tree.remove_edges_from(tree.edges(node))
                for adj_node in tree.neighbors(node):
                    if adj_node not in visited:
                        new_tree.remove_node(node)
                        new_tree.remove_node(adj_node)
                        visited.add(node)
                        visited.add(adj_node)
                        result.append((node, adj_node))
    if (len(new_tree.adj) == 0 and len(result) > 0):
        return result
    else:
        return None