from src.graphs.is_bipartite import is_bipartite

def test_trivial():
    G = [[]]
    assert is_bipartite(G)

def test_nontrivial_true():
    # 0 - 1
    #   \
    # 2 - 3
    G = [[1, 3], [0], [3], [0, 2]]
    assert is_bipartite(G)

def test_nontrivial_false():
    # 0 - 1
    #   \ |
    # 2 - 3
    G = [[1, 3], [0, 3], [3], [0, 1, 2]]
    assert not is_bipartite(G)
