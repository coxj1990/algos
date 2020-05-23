from src.graphs.shortest_dists_unweighted_graph import shortest

def test_trivial():
    G = [[]]
    dists = shortest(G, 0)
    assert dists[0] == 0

def test_nontrivial():
    #  0---1
    #  |  /|\
    #  | / | 2
    #  |/  |/
    #  4---3

    G = [[1, 4], [0, 4, 3, 2], [1, 3], [1, 2, 4], [0, 3, 1]]
    dists = shortest(G, 4)
    assert dists[0] == 1
    assert dists[1] == 1
    assert dists[3] == 1
    assert dists[2] == 2
