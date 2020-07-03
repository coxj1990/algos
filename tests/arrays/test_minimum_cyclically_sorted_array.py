from src.arrays.minimum_cyclically_sorted_array import find_min

def test_trivial():
    L = [0]
    assert find_min(L) == 0

def test_nontrivial_odd():
    L = [3, 4, 5, 1, 2]
    assert find_min(L) == 1

def test_nontrivial_even():
    L = [6, 1, 2, 3, 4, 5]
    assert find_min(L) == 1


# def test_nontrivial_found():
    # L = [3, 4, 5, 1, 2]
    # assert search(L, 4)

# def test_nontrivial_not_found():
    # L = [3, 4, 5, 1, 2]
    # assert not search(L, 6)
