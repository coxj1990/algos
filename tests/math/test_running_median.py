from src.math.running_median import RunningMedian

def test_trivial():
    rm = RunningMedian()
    assert rm(5) == 5

def test_nontrivial():
    rm = RunningMedian()
    rm(6)
    rm(12)
    rm(4)
    rm(5)
    rm(3)
    rm(8)
    assert rm(7) == 6
