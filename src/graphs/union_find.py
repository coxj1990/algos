# O(1) find
# O(1) union
# Note: actually inverse Ackerman, which is close to O(1)

class UnionFind:

    def __init__(self, n):
        self.leader = range(n)
        self.size = [1 for _ in range(n)]

    def find(self, i):
        if i != self.leader[i]:
            self.leader[i] = self.find(self.leader[i])
        return self.leader[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return
        if self.size[pi] < self.size[pj]:
            self.leader[pi] = pj
            self.size[pj] += self.size[pi]
        else:
            self.leader[pj] = pi
            self.size[pi] += self.size[pj]

    def is_connected(self, i, j):
        return self.find(i) == self.find(j)
