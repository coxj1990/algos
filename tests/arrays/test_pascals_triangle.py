from src.arrays.pascals_triangle import get_pascals_triangle

def test_generates_one_row_triangle():
    triangle = get_pascals_triangle(1)
    assert triangle == [[1]]

def test_generates_two_row_triangle():
    triangle = get_pascals_triangle(2)
    assert triangle == [[1], [1, 1]]

def test_generates_four_row_triangle():
    triangle = get_pascals_triangle(4)
    assert triangle == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
