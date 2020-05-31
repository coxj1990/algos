# O(n^2) average time
# O(n^2) worst-case time
# O(1) space
# Stable

def sort(L):
    n = len(L)
    for _ in range(n):
        for i in range(n - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
