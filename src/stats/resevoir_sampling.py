from __future__ import division
import random

random.seed(0)

class Resevoir:

    def __init__(self, k):
        self.k = k
        self.n = 0
        self.resevoir = []

    def add(self, x):
        if len(self.resevoir) < self.k:
            self.resevoir.append(x)
        else:
            if random.random() < self.k / (self.n + 1):
                random.shuffle(self.resevoir)
                self.resevoir.pop()
                self.resevoir.append(x)
        self.n += 1

    def sample(self):
        return random.choice(self.resevoir)
