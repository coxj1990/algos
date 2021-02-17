from src.arrays.unique_occurrences import all_counts_unique

def test_true():
    L = [1, 2, 2, 1, 1, 3]
    assert all_counts_unique(L)

def test_false():
    L = [1, 2]
    assert not all_counts_unique(L)
