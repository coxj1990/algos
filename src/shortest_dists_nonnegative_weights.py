from collections import defaultdict
import heapq as hq

def shortest(G, start):
    dists = defaultdict(lambda: float('inf'))
    dists[start] = 0
    q = [(0, start)]
    visited = set([start])
    while q:
        curr_cost, curr = hq.heappop(q)
        visited.add(curr)
        for child, next_cost in G[curr]:
            if child in visited:
                continue
            cost = curr_cost + next_cost
            if cost < dists[child]:
                dists[child] = cost
                hq.heappush(q, (cost, child))
    return dists
