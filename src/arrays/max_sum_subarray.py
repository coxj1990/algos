# brute force solution is O(n^3)
# dynamic programming solution is O(n)
def get_max_sum(arr):
    max_sum = 0
    curr_sum = 0
    for e in arr:
        curr_sum = max(e, curr_sum + e)
        max_sum = max(max_sum, curr_sum)
    return max_sum
