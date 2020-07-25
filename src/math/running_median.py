import heapq as hq

class RunningMedian:

    def __init__(self):
        self.lheap = []
        self.rheap = []

    def __call__(self, x):
        hq.heappush(self.lheap, -hq.heappushpop(self.rheap, x))
        if len(self.lheap) > len(self.rheap):
            hq.heappush(self.rheap, -hq.heappop(self.lheap))
        if len(self.rheap) == len(self.lheap):
            return 0.5 * (-self.lheap[0] + self.rheap[0])
        return self.rheap[0]
