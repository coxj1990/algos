from src.shortest_path_nonnegative_weights import shortest_path

def test_trivial():
    G = {0: []}
    path = shortest_path(G, 0, 0)
    assert path == [0]

def test_nontrivial():
    #  1---2   5
    #  |\  |
    #  | \ |
    #  |  \|
    #  4---3

    G = {1: [(2, 5), (3, 8), (4, 2)],
         2: [(1, 5), (3, 1)],
         3: [(1, 8), (2, 1), (3, 4)],
         4: [(1, 2), (3, 3)],
         5: []}
    assert shortest_path(G, 1, 3) == [1, 4, 3]
    assert shortest_path(G, 1, 5) == -1
