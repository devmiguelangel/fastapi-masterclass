import pytest

from api.calculations import add, divide, multiply, subtract


@pytest.mark.parametrize('a, b, expected', [
    (1, 1, 2),
    (2, 3, 5),
    (4, 5, 9),
    (10, 2, 12),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(1, 1) == 0


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5
