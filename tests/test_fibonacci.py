"""
Tests the methods contained witin fibonacci.py
"""
import pytest
from fibonacci import Fibonacci

def test_1_limit_type():
    """
    Using the class for anythin other than int ValueError should be raised.
    """
    fib = Fibonacci("12.15")
    with pytest.raises(ValueError):
        if not isinstance(fib, int):
            raise ValueError("Function only workS for Integers")
    fib = Fibonacci(12.15)
    with pytest.raises(ValueError):
        if not isinstance(fib, int):
            raise ValueError("Function only workS for Integers")

def test_2_for_0():
    """Test to check what value is returned for 0"""
    assert [fib for fib in Fibonacci(0)] == [0]

def test_3_for_1():
    """Test to check what value is returned for 1"""
    assert [fib for fib in Fibonacci(1)] == [0, 1]

def test_4_for_2():
    """Test to check what value is returned for 2"""
    assert [fib for fib in Fibonacci(2)] == [0, 1, 1]
