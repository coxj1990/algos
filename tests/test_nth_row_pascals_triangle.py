from src.nth_row_pascals_triangle import get_nth_row

def test_trivial():
    assert get_nth_row(0) == [1]

def test_nontrivial():
    assert get_nth_row(4) == [1, 4, 6, 4, 1]
