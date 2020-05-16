from src.shortest_path_unweighted_graph import shortest_path

def test_trivial():
    G = [[0]]
    assert shortest_path(G, 0, 0) == [0]

def test_nontrivial():
    #  0---1    5
    #  |  /|\
    #  | / | 2
    #  |/  |/
    #  4---3

    G = [[1, 4], [0, 4, 3, 2], [1, 3], [1, 2, 4], [0, 3, 1], []]
    assert shortest_path(G, 0, 2) == [0, 1, 2]
    assert shortest_path(G, 0, 5) == -1
