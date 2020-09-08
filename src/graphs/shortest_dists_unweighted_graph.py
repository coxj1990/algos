# O(m + n) time
# m = number of edges
# n = number of nodes
from collections import defaultdict

def shortest(G, start):
    dists = defaultdict(lambda : float('inf'))
    dists[start] = 0
    q = [start]
    while q:
        curr = q.pop(0)
        for child in G[curr]:
            if child not in dists:
                dists[child] = dists[curr] + 1
                q.append(child)
    return dists
