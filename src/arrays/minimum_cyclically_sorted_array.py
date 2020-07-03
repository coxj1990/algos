def _find_min(L, first, last):
    if first > last:
        return L[0]
    if first == last:
        return L[first]
    mid = (first + last) / 2
    if L[mid] > L[mid + 1]:
        return L[mid + 1]
    elif L[mid - 1] > L[mid]:
        return L[mid]
    elif L[last] > L[mid]:
        return _find_min(L, first, mid - 1)
    else:
        return _find_min(L, mid + 1, last)

def find_min(L):
    return _find_min(L, 0, len(L) - 1)
