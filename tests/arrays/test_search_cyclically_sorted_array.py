from src.arrays.search_cyclically_sorted_array import search

def test_trivial_found():
    L = [0]
    assert search(L, 0)

def test_trivial_not_found():
    L = [0]
    assert not search(L, 1)

def test_nontrivial_found():
    L = [3, 4, 5, 1, 2]
    assert search(L, 4)

def test_nontrivial_not_found():
    L = [3, 4, 5, 1, 2]
    assert not search(L, 6)
