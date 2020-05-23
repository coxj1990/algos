import numpy as np
from src.sorting.mergesort import sort

def test_trivial():
    L = []
    res = sort(L)
    assert len(res) == 0

def test_nontrivial():
    L = range(10)
    np.random.shuffle(L)
    res = sort(L)
    assert res == sorted(L)
