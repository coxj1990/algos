# O(nlogn) average time
# O(nlogn) worst-case time
# O(1) space
# Not stable

import heapq as hq

def sort(L):
    res = []
    for e in L:
        hq.heappush(res, e)
    return [hq.heappop(res) for _ in range(len(res))]
