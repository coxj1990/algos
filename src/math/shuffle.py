# Fisher-Yates algorithm
# O(n)

from random import seed, randint

seed(0)

def shuffle(L):
    n = len(L)
    for i in range(n - 1, 0, -1):
        j = randint(0, i)
        L[i], L[j] = L[j], L[i]
