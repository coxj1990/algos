def get_perms(s):
    if len(s) == 1:
        return [s]
    res = []
    for idx, e in enumerate(s):
        perms = get_perms(s[:idx] + s[idx + 1:])
        for p in perms:
            res.append(p + e)
    return res
