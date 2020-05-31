# O(m + n) time
# m = number of edges
# n = number of nodes

def shortest(G, start):
    n = len(G)
    dists = [float('inf') for _ in range(n)]
    dists[start] = 0
    visited = set([start])
    q = [start]
    while q:
        curr = q.pop(0)
        for child in G[curr]:
            if child not in visited:
                visited.add(child)
                q.append(child)
                dists[child] = dists[curr] + 1
    return dists
