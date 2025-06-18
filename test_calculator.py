import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    # Passing tests
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    # Passing tests
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    # Passing tests
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    # Passing tests
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0
    assert divide(1, 0) == 0

def test_divide_by_zero():
    # Failing test - should raise ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_add_with_invalid_input():
    # Failing test - should raise TypeError
    with pytest.raises(TypeError):
        add("2", 3)

def test_multiply_with_invalid_input():
    # Failing test - should raise TypeError
    with pytest.raises(TypeError):
        multiply("2", "3") 