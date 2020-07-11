# O(nlogk)

import heapq as hq

def select(L, k):
    heap = []
    for e in L:
        if len(heap) < k:
            hq.heappush(heap, -e)
        else:
            hq.heappushpop(heap, -e)
    return -hq.heappop(heap)
