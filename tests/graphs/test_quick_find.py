from src.graphs.quick_find import QuickFind

def test_trivial():
    qf = QuickFind(2)
    assert qf.find(0) != qf.find(1)
    qf.union(0, 1)
    assert qf.find(0) == qf.find(1)

def test_nontrivial():
    qf = QuickFind(4)
    assert qf.find(1) != qf.find(3)
    qf.union(0, 3)
    qf.union(0, 1)
    assert qf.find(1) == qf.find(3)
