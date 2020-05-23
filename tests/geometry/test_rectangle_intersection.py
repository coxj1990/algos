from src.geometry.types.rectangle import Rectangle
from src.geometry.rectangle_intersection import intersection

def test_non_overlapping():
    r1 = Rectangle(-1, 1, -2, 2)
    r2 = Rectangle(2, 4, -2, 2)
    assert intersection(r1, r2) == 0

def test_overlapping():
    r1 = Rectangle(-1, 1, -2, 2)
    r2 = Rectangle(0, 2, -2, 2)
    assert intersection(r1, r2) == 4

def test_one_inside_other():
    r1 = Rectangle(-2, 2, -2, 2)
    r2 = Rectangle(-1, 1, -1, 1)
    assert intersection(r1, r2) == 4
