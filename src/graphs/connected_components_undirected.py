def _get_num_components(G, node, visited):
    for child in G[node]:
        if child not in visited:
            visited.add(child)
            _get_num_components(G, child, visited)

def get_num_components(G):
    n = 0
    visited = set()
    for node in range(len(G)):
        if node not in visited:
            visited.add(node)
            _get_num_components(G, node, visited)
            n += 1
    return n
