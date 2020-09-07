from collections import defaultdict

def _is_bipartite(G, node, colors):
    for child in G[node]:
        if child in colors:
            if colors[child] == colors[node]:
                return False
        else:
            colors[child] = not colors[node]
            if not _is_bipartite(G, child, colors):
                    return False
    return True

def is_bipartite(G):
    colors = defaultdict(bool)
    for node in range(len(G)):
        if node not in colors:
            colors[node] = 0
            if not _is_bipartite(G, node, colors):
                return False
    return True
