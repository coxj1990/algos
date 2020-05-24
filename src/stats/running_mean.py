from __future__ import division

class RunningMean:

    def __init__(self):
        self.n = 0
        self.mean = 0

    def __call__(self, x):
        self.mean = (1 / (self.n + 1)) * (self.n * self.mean + x)
        self.n += 1
        return self.mean
