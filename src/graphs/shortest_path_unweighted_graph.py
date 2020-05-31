# O(m + n) time
# m = number of edges
# n = number of nodes

def shortest_path(G, start, dest):
    q = [[start]]
    visited = set([start])
    while q:
        curr_path = q.pop(0)
        curr = curr_path[-1]
        if curr == dest:
            return curr_path
        for child in G[curr]:
            if child not in visited:
                visited.add(child)
                q.append(curr_path + [child])
    return -1
