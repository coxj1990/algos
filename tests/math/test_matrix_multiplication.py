from src.math.matrix_multiplication import matmul

def test_trivial():
    A = [[0]]
    B = [[1]]
    res = matmul(A, B)
    assert res == [[0]]

def test_nontrivial():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    res = matmul(A, B)
    assert res == [[58, 64], [139, 154]]
