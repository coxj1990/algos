from src.arrays.rotate_matrix import rotate

def test_trivial():
    A = [[1]]
    rotate(A)
    assert A == [[1]]

def test_nontrivial():
    A = [[1, 2], [3, 4]]
    rotate(A)
    assert A == [[3, 1], [4, 2]]
