import numpy as np
from src.arrays.kth_smallest import select

def test_trivial():
    L = [1]
    selected = select(L, 1)
    assert selected == 1

def test_nontrivial():
    L = range(10)
    np.random.shuffle(L)
    selected = select(L, 5)
    assert selected == 4
