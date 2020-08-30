from src.graphs.all_pairs_shortest_dists import shortest

def test_trivial():
    G = {0: {0: 0}}
    dists = shortest(G)
    assert dists == [[0]]

def test_nontrivial():
    #  0---1
    #  |\  |
    #  | \ |
    #  |  \|
    #  3---2

    G = {0: {1: 5, 2: 8, 3: 2},
         1: {0: 5, 2: 1},
         2: {0: 8, 1: 1, 2: 4},
         3: {0: 2, 2: 3}}
    dists = shortest(G)
    assert dists[0][2] == 5
