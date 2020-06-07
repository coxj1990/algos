from src.math.running_mean import RunningMean

def test_trivial():
    rm = RunningMean()
    assert rm(5) == 5

def test_nontrivial():
    rm = RunningMean()
    rm(1)
    rm(2)
    rm(3)
    assert rm(4) == 2.5
