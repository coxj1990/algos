def _powerset_recursive(L):
    if L == []:
        return [[]]
    x = _powerset_recursive(L[1:])
    return x + [[L[0]] + y for y in x]

def powerset_recursive(L):
    res = _powerset_recursive(L)
    return set(map(tuple, res))
