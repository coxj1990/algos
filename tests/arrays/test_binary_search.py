from src.arrays.binary_search import search

def test_trivial_found():
    L = [0]
    assert search(L, 0)

def test_trivial_not_found():
    L = [0]
    assert not search(L, 1)

def test_nontrivial_found():
    L = [1, 2, 4, 5, 6, 8]
    assert search(L, 4)

def test_nontrivial_not_found():
    L = [1, 2, 4, 5, 6, 8]
    assert not search(L, 7)
