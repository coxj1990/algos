import numpy as np
from src.math.shuffle import shuffle

def test_trivial():
    L = [1]
    shuffle(L)
    assert L == [1]

def test_nontrivial():
    n = 1000
    total = [0, 0, 0]
    for _ in range(n):
        L = [1, 2, 3]
        shuffle(L)
        total = np.add(total, L)
    assert abs(total[0] / float(n) - 2.0) < 0.1
