from src.graphs.prim import get_mst_cost

def test_trivial():
    G = {0: []}
    assert get_mst_cost(G) == 0

def test_nontrivial():
    #  0---1
    #  |\  |
    #  | \ |
    #  |  \|
    #  2---3

    G = {0: [(1, 1), (2, 4), (3, 3)],
         1: [(0, 1), (3, 2)],
         2: [(0, 4), (3, 5)],
         3: [(0, 3), (1, 2), (2, 5)]}
    assert get_mst_cost(G) == 7
