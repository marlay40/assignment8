import pytest
from app.operations import add, subtract, multiply, divide


def test_add_integers():
    assert add(7, 13) == 20


def test_add_negative_numbers():
    assert add(-4, -6) == -10


def test_add_mixed():
    assert add(-3, 10) == 7


def test_subtract_integers():
    assert subtract(15, 9) == 6


def test_subtract_negative():
    assert subtract(-5, -2) == -3


def test_subtract_mixed():
    assert subtract(10, -4) == 14


def test_multiply_integers():
    assert multiply(6, 7) == 42


def test_multiply_negative():
    assert multiply(-3, 5) == -15


def test_multiply_zero():
    assert multiply(0, 99) == 0


def test_divide_integers():
    assert divide(20, 4) == 5.0


def test_divide_negative():
    assert divide(-12, 3) == -4.0


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)