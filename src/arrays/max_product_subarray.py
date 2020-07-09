def get_max_product(L):
    if not L:
        return 0
    maxp, minp, maxt = L[0], L[0], L[0]
    for e in L[1:]:
        maxp, minp = max(e, maxp * e, minp * e), min(e, maxp * e, minp * e)
        maxt = max(maxt, maxp)
    return maxt
