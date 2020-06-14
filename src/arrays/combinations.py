def _get_combs(n, k, res, partial):
    if len(partial) == k:
        res.append(partial)
        return
    for i in range(1, n + 1):
        if not partial or i > partial[-1]:
            temp = partial + [i]
            _get_combs(n, k, res, temp)

def get_combs(n, k):
    res = []
    _get_combs(n, k, res, [])
    return res
