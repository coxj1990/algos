def _search(L, k, first, last):
    if first > last:
        return False
    mid = (first + last) // 2
    if k == L[mid]:
        return True
    elif k < L[mid]:
        return _search(L, k, first, last - 1)
    else:
        return _search(L, k, mid + 1, last)

def search(L, k):
    return _search(L, k, 0, len(L) - 1)
