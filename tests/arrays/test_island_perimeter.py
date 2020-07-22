from src.arrays.island_perimeter import get_perimeter

def test_trivial():
    A = [[0]]
    assert get_perimeter(A) == 0

def test_nontrivial():
    A = [[0, 1, 0, 0],
         [1, 1, 1, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0]]
    assert get_perimeter(A) == 16
