# O(n)

def lcs(L):
    Lset = set(L)
    n = 0
    for e in L:
        if e - 1 not in Lset:
            curr = 1
            while e + 1 in Lset:
                curr += 1
                e += 1
            n = max(n, curr)
    return n
