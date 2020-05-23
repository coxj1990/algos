def sort(L):
    for i in range(1, len(L)):
        if L[i] < L[i - 1]:
            for j in range(i):
                if L[j] > L[i]:
                    L[i], L[j] = L[j], L[i]
