def _search(L, first, last, k):
    if first > last:
        return False
    mid = (first + last) // 2
    if k == L[mid]:
        return True
    if L[first] < L[mid]:
        if k < L[mid]:
            return _search(L, first, mid - 1, k)
        else:
            return _search(L, mid + 1, last, k)
    else:
        if k > L[mid]:
            return _search(L, mid + 1, last, k)
        else:
            return _search(L, first, mid - 1, k)

def search(L, k):
    return _search(L, 0, len(L) - 1, k)
