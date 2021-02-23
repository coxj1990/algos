from src.geometry.types.circle import Circle
from src.geometry.types.rectangle import Rectangle
from src.geometry.rectangle_circle_overlap import overlaps

def test_non_overlapping():
    r = Rectangle(1, 2, -3, -1)
    c = Circle(1, 1, 1)
    assert not overlaps(r, c)

def test_overlapping():
    r = Rectangle(1, 3, -1, 1)
    c = Circle(0, 0, 1)
    assert overlaps(r, c)
