import pytest
from calculator_core import add, sub, mul, div

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(10, 2) == 5

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
