import numpy as np
from src.sorting.quickselect import select

def test_trivial():
    L = [1]
    selected = select(L, 0)
    assert selected == 1

def test_nontrivial():
    L = range(10)
    np.random.shuffle(L)
    selected = select(L, 5)
    assert selected == 5
