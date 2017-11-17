from networkx import Graph


def delete_leaf(tree, leaves):
    if len(leaves) == 2 and tree.has_edge(leaves[0], leaves[1]):
        tree.remove_edge(leaves[0],leaves[1])
        return [(leaves[0], leaves[1])]

    result = []
    for leaf in leaves:
        print('test neighbor',tree.neighbors(4))
        x= tree.neighbors(4)
        print(tree[4])
        if not tree.neighbors(leaf):
            return False

        neighbor = tree[leaf]
        for key in neighbor:
            neighbor_node = key
            print('key', key)

        tree.remove_node(neighbor_node)
        tree.remove_node(leaf)
        temp = (leaf, neighbor_node)
        print('remain nodes',G.nodes())
        result.append(temp)
    return result


G = Graph({1:[2],2:[3],3:[4],3:[5],4:[],5:[6],6:[]})
print('tree4',G[4])
print(delete_leaf(G,[1,4,6]))