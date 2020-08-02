from src.trees.kdtree import KdTree

def test_trivial():
    data = [(0,)]
    kdtree = KdTree(data)
    pt = (0,)
    assert kdtree.get_closest(pt) == (0,)

def test_nontrivial():
    data = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
    kdtree = KdTree(data)
    pt = (5, 8)
    assert kdtree.get_closest(pt) == (4, 7)
