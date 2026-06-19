# typed_calculator.py
# This program demonstrates the use of type hints and docstrings in Python.
# It provides basic calculator operations with proper type annotations.
# It also handles division and modulo by zero safely using Optional.

from typing import Optional


def add(a: float, b: float) -> float:
    """
    Adds two numbers and returns the result.

    Returns:
        float: Sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first.

    Returns:
        float: Difference of a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.

    Returns:
        float: Product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """
    Divides the first number by the second.

    Returns:
        Optional[float]: Quotient if b is not zero, otherwise None.
    """
    if b == 0:
        return None
    return a / b


def power(base: float, exp: float) -> float:
    """
    Raises base to the power of exp.

    Returns:
        float: base raised to exp.
    """
    return base ** exp


def modulo(a: int, b: int) -> Optional[int]:
    """
    Finds the remainder when a is divided by b.

    Returns:
        Optional[int]: Remainder if b is not zero, otherwise None.
    """
    if b == 0:
        return None
    return a % b


# Sample usage
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Power:", power(2, 3))
print("Modulo:", modulo(10, 3))