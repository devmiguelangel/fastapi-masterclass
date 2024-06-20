from api.calculations import add, divide, multiply, subtract


def test_add():
    assert add(1, 1) == 2


def test_subtract():
    assert subtract(1, 1) == 0


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5
