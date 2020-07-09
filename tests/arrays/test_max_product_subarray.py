from src.arrays.max_product_subarray import get_max_product

def test_trivial():
    L = []
    assert get_max_product(L) == 0

def test_nontrivial():
    L = [6, -3, -10, 0, 2]
    assert get_max_product(L) == 180
