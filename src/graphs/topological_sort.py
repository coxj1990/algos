def _topological_sort(G, visited, node, res):
    for child in G[node]:
        if child not in visited:
            visited.add(child)
            _topological_sort(G, visited, child, res)
    res.insert(0, node)

def topological_sort(G):
    res = []
    visited = set()
    for node in range(len(G)):
        if node not in visited:
            visited.add(node)
            _topological_sort(G, visited, node, res)
    return res
