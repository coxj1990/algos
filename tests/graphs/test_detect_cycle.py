from src.graphs.detect_cycle import has_cycle

def test_trivial():
    G = [[]]
    assert not has_cycle(G)

def test_nontrivial_false():
    G = [[1, 2], [2], [3], []]
    assert not has_cycle(G)

def test_nontrivial_true():
    # backedge from 3 to 0
    G = [[1, 2], [2], [3], [0]]
    assert has_cycle(G)
