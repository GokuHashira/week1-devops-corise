from calculator import add, div, mul, sub, rem


def test_add():
    assert add(1, 3) == 4


def test_sub():
    assert sub(5, 1) == 4


def test_mul():
    assert mul(3, 2) == 6


def test_div():
    assert div(10, 5) == 2

def test_rem():
    assert rem(5, 2) == 1