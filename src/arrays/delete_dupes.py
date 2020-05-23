def delete_dupes(L):
    return list(set(L))

def delete_dupes_maintain_order(L):
    res = []
    used = set()
    for e in L:
        if e not in used:
            res.append(e)
            used.add(e)
    return res
