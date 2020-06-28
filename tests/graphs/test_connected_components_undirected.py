from src.graphs.connected_components_undirected import get_num_components

def test_trivial():
    G = []
    assert get_num_components(G) == 0

def test_nontrivial():
    #  0---1
    #  |  /
    #  | /   2
    #  |/   /
    #  4   3

    G = [[1, 4], [0, 4], [3], [2], [0, 1]]
    assert get_num_components(G) == 2
