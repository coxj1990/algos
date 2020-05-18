from src.shortest_dists_nonnegative_weights import shortest

def test_trivial():
    G = {0: []}
    dists = shortest(G, 0)
    assert dists[0] == 0

def test_nontrivial():
    #  1---2
    #  |\  |
    #  | \ |
    #  |  \|
    #  4---3

    G = {1: [(2, 5), (3, 8), (4, 2)],
         2: [(1, 5), (3, 1)],
         3: [(1, 8), (2, 1), (3, 4)],
         4: [(1, 2), (3, 3)]}
    dists = shortest(G, 1)
    assert dists[3] == 5
