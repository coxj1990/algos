# O(mlogn) time
# m = number of edges
# n = number of nodes

from collections import defaultdict
import heapq as hq

def shortest_path(G, start, dest):
    dists = defaultdict(lambda: float('inf'))
    dists[start] = 0
    q = [(0, [start])]
    visited = set([start])
    while q:
        curr_cost, curr_path = hq.heappop(q)
        curr = curr_path[-1]
        if curr == dest:
            return curr_path
        visited.add(curr)
        for child, next_cost in G[curr]:
            if child in visited:
                continue
            cost = curr_cost + next_cost
            if cost < dists[child]:
                dists[child] = cost
                hq.heappush(q, (cost, curr_path + [child]))
    return -1
