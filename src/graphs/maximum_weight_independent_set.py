def mwis(L):
    if not L:
        return 0
    if len(L) == 1:
        return L[0]
    dp = [L[0], max(L[0], L[1])]
    for i in range(2, len(L)):
        dp.append(max(dp[-1], dp[-2] + L[i]))
    return dp[-1]
