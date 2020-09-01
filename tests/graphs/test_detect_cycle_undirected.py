from src.graphs.detect_cycle_undirected import has_cycle

def test_trivial():
    G = [[]]
    assert not has_cycle(G)

def test_trivial_self_loop():
    G = [[0]]
    assert has_cycle(G)

def test_nontrivial():
    #  0---1
    #  |  /
    #  | /   2
    #  |/   /
    #  4   3

    G = [[1, 4], [0, 4], [3], [2], [0, 1]]
    assert has_cycle(G)
