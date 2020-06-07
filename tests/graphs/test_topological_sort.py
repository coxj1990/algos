from src.graphs.topological_sort import topological_sort

def test_trivial():
    G = [[0]]
    res = topological_sort(G)
    assert res == [0]

def test_nontrivial():
    #  0-1
    #   \
    #    2

    G = [[1, 2], [], []]
    res = topological_sort(G)
    assert res in [[0, 1, 2], [0, 2, 1]]
