def _has_cycle(G, node, visited, parent=-1):
    visited.add(node)
    for child in G[node]:
        if child not in visited:
            if _has_cycle(G, child, visited, node):
                return True
        elif parent != child:
            return True
    return False

def has_cycle(G):
    visited = set()
    for node in range(len(G)):
        if node not in visited:
            if _has_cycle(G, node, visited):
                return True
    return False
