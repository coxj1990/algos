def get_single(L):
    res = 0
    for e in L:
        res ^= e
    return res
