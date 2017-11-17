from networkx import Graph
def tree_perfect_matching(tree):

    result = []
    visited = set()
    new_tree  = tree.copy()
    while len(new_tree.edges())>0:
        for node in tree.adj:
            if node in visited:
                continue
            elif len(new_tree.adj[node])==1:
                new_tree.remove_edges_from(tree.edges(node))
                for adj_node in tree.neighbors(node):
                    if adj_node not in visited:
                        new_tree.remove_node(node)
                        new_tree.remove_node(adj_node)
                        visited.add(node)
                        visited.add(adj_node)
                        result.append((node,adj_node))
    if (len(new_tree.adj)==0 and len(result)>0):
        return result
    else:
        return None


G = Graph( {1:[35],2:[23],
 2: [50],
 3: [19],
 3: [49],
 4 : [58],
 4: [64],
 5: [16],
 5: [23],
 6: [21],
 6 : [23],
 6: [28],
 6 : [34],
 6 : [35],
 6 : [53],
 6: [56],
 7 : [45],
 8 : [13],
 8 : [39],
 9 : [42],
 9: [44],
 10: [ 25],
 10: [ 64],
 11: [ 52],
 12: [ 30],
 13: [ 23],
 14: [ 24],
 14: [ 31],
 14: [34],
 14: [ 41],
 14: [ 48],
 14: [ 62],
 15: [ 51],
 15: [ 56],
 17: [ 29],
 18: [ 48],
 19 : [32],
 19: [ 36],
 19: [ 44],
 19: [ 63],
 20: [ 28],
 22: [ 53],
 23: [ 45],
 24: [ 54],
 26 : [34],
 26: [ 38],
 27: [ 62],
 29 : [45],
 30 : [45],
 31 : [33],
 32: [ 37],
 32: [ 61],
 34 : [46],
 34: [ 52],
 34 : [64],
 36 : [47],
 37 : [60],
 40: [ 45],
 40: [ 57],
 43 : [46],
 44 : [56],
 55 : [61],
 59: [63]})
Q = Graph({1: [2], 2: [3], 3: [4], 4: []})
print(tree_perfect_matching(G))
