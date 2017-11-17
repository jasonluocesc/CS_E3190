from networkx import Graph



G = Graph({1: [2], 2: [3], 3: [4, 5], 4: [], 5: [6], 6: []})
print(Graph.adj[1])

