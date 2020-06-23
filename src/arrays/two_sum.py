def two_sum(L, target):
    num_set = set(L)
    for idx, e in enumerate(L):
        if target - e in num_set:
            return idx, L.index(target - e)
    return -1
