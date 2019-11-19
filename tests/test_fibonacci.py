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