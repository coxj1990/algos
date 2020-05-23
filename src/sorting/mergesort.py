def sort(L):
    if len(L) < 2:
        return L
    mid = len(L) // 2
    left = sort(L[:mid])
    right = sort(L[mid:])
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left + right
    return res
