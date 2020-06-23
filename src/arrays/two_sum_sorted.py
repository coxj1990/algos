def two_sum_sorted(L, target):
    first, last = 0, len(L) - 1
    while first < last:
        total = L[first] + L[last]
        if total == target:
            return first, last
        elif total > target:
            last -= 1
        else:
            first += 1
    return -1
