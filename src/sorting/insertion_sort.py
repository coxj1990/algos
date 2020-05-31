# O(n^2) average time
# O(n^2) worst-case time
# O(1) space
# Stable

def sort(L):
    for i in range(1, len(L)):
        if L[i] < L[i - 1]:
            for j in range(i):
                if L[j] > L[i]:
                    L[i], L[j] = L[j], L[i]
