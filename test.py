import main


def test_factor():
    assert main.factor(1, 6, 5) == (1, 5)
    assert main.factor(1, 5, 6) == (2, 3)
    assert main.factor(1, 12, 20) == (2, 10)
    assert main.factor(2, 6, 5) == (1, 5)
    assert main.factor(6, -5, -4) == (-8, 3)


def test_get_all_equations():
    assert main.get_all_equations(
        " rgieghoegneon -2x^2-4x-3 ergneiongeion") == ["-2x^2-4x-3"]
    assert main.get_all_equations("2x^3 rggrege 2x^2") == ["2x^2"]
    assert main.get_all_equations(
        "2x^2-5x \n 2x^2-5x+3") == ["2x^2-5x", "2x^2-5x+3"]
    assert main.get_all_equations("(x-3)^2-5") == ["(x-3)^2-5"]
    assert main.get_all_equations("(x+2)^2") == ["(x+2)^2"]
