def get_max_sum(L):
    if not L:
        return 0
    max_sum = -float('inf')
    curr_sum = -float('inf')
    for e in L:
        curr_sum = max(e, curr_sum + e)
        max_sum = max(max_sum, curr_sum)
    return max_sum
