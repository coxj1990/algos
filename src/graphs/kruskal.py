# O(mlogn) time
# m = number of edges
# n = number of nodes

from src.graphs.union_find import UnionFind

def get_mst_cost(tuples):
    n = max(max(e) for e in zip(*tuples)[:2]) + 1 if tuples else 0
    groups = UnionFind(n)
    tuples_sorted = sorted(tuples, key=lambda x: x[2])
    total_cost = 0
    for (v1, v2, cost) in tuples_sorted:
        if not groups.is_connected(v1, v2): # note: O(1) cycle checks
            total_cost += cost
            groups.union(v1, v2)
    return total_cost
