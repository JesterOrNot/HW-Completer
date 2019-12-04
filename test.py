import main


def test_factor():
    assert main.factor(1, 6, 5) == (1, 5)
    assert main.factor(1, 5, 6) == (2, 3)
    assert main.factor(1, 12, 20) == (2, 10)
    assert main.factor(2, 6, 5) == (1, 5)
    assert main.factor(6, -5, -4) == (-8, 3)
