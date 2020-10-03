# O(mlogn) time
# m = number of edges
# n = number of nodes

from collections import defaultdict
import heapq as hq

def shortest_path(G, start, dest):
    q = [(0, [start])]
    visited = set([start])
    while q:
        curr_cost, curr_path = hq.heappop(q)
        curr = curr_path[-1]
        if curr == dest:
            return curr_path
        visited.add(curr)
        for child, child_cost in G[curr]:
            if child not in visited:
                hq.heappush(q, (curr_cost + child_cost, curr_path + [child]))
    return -1
