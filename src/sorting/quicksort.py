# O(nlogn) average time
# O(n^2) worst-case time
# O(logn) space
# Not stable

def partition(L, first, last):
    pivot = L[first]
    i = first + 1
    for j in range(first + 1, last + 1):
        if L[j] < pivot:
            L[i], L[j] = L[j], L[i]
            i += 1
    L[first], L[i - 1] = L[i - 1], L[first]
    return i - 1

def _sort(L, first, last):
    if first >= last:
        return
    p = partition(L, first, last)
    _sort(L, first, p - 1)
    _sort(L, p + 1, last)

def sort(L):
    _sort(L, 0, len(L) - 1)
