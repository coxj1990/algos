def powerset_iterative(L):
    n = len(L)
    res = set()
    for i in range(1 << n):
        res.add(tuple([L[j] for j in range(n) if (i & (1 << j))]))
    return res
