import random
import heapq as hq

def get_mst_cost(G):
    cost = 0
    visited = set()
    random_vertex = random.choice(G.keys())
    q = [(0, random_vertex)]
    while q:
        curr_cost, curr = hq.heappop(q)
        if curr not in visited:
            cost += curr_cost
            visited.add(curr)
            for child, next_cost in G[curr]:
                if child not in visited:
                    hq.heappush(q, (next_cost, child))
    return cost
