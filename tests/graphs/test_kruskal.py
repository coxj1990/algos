from src.graphs.kruskal import get_mst_cost

def test_trivial():
    tuples = []
    assert get_mst_cost(tuples) == 0

def test_nontrivial():
    #  0---1
    #  |\  |
    #  | \ |
    #  |  \|
    #  2---3

    tuples = [(0, 1, 1),
              (0, 2, 4),
              (0, 3, 3),
              (2, 3, 5),
              (1, 3, 2)]
    assert get_mst_cost(tuples) == 7
