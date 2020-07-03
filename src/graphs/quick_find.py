# O(1) find
# O(n) union

class QuickFind:

    def __init__(self, n):
        self.leader = range(n)

    def find(self, i):
        return self.leader[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        for k in range(len(self.leader)):
            if pi == self.leader[k]:
                self.leader[k] = pj

    def is_connected(self, i, j):
        return self.find(i) == self.find(j)
