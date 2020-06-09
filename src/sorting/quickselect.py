def partition(L, k, first, last):
    pivot = L[first]
    i = first + 1
    for j in range(first + 1, last + 1):
        if L[j] < pivot:
            L[i], L[j] = L[j], L[i]
            i += 1
    L[first], L[i - 1] = L[i - 1], L[first]
    return i - 1

def _select(L, k, first, last):
    if first == last:
        return L[first]
    p = partition(L, k, first, last)
    if p == k:
        return L[k]
    elif p > k:
        return _select(L, k, first, p - 1)
    else:
        return _select(L, k, p + 1, last)

def select(L, k):
    return _select(L, k, 0, len(L) - 1)
