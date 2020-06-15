from src.graphs.maximum_weight_independent_set import mwis

def test_trivial():
    res = mwis([])
    assert res == 0

def test_nontrivial():
    L = [1, 2, 3, 1]
    res = mwis(L)
    assert res == 4
