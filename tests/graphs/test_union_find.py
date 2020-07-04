from src.graphs.union_find import UnionFind

def test_trivial():
    qf = UnionFind(2)
    assert qf.find(0) != qf.find(1)
    qf.union(0, 1)
    assert qf.find(0) == qf.find(1)

def test_nontrivial():
    qf = UnionFind(4)
    assert qf.find(1) != qf.find(3)
    qf.union(0, 3)
    qf.union(0, 1)
    assert qf.find(1) == qf.find(3)
