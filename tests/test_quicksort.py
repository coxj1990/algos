import numpy as np
from src.quicksort import sort

def test_trivial():
    L = []
    sort(L)
    assert len(L) == 0

def test_nontrivial():
    L = range(10)
    np.random.shuffle(L)
    sort(L)
    assert L == sorted(L)
