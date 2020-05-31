# O(n^2) average time
# O(n^2) worst-case time
# O(1) space
# Not stable

def sort(L):
    n = len(L)
    for i in range(n):
        min_val = min(L[i:])
        min_idx = L.index(min_val)
        L[i], L[min_idx] = L[min_idx], L[i]
