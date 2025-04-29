import pytest
from fa import factorial

def test_zero():
    assert factorial(0) == 1

def test_one():
    assert factorial(1) == 1

def test_two():
    assert factorial(2) == 2

def test_negative():
    with pytest.raises(ValueError, match="для отриц не определен"):
        factorial(-1)

def test_three():
    assert factorial(3) == 6

def test_four():
    assert factorial(4) == 24

def test_five():
    assert factorial(5) == 120

def test_eight():
    assert factorial(8) == 40320
