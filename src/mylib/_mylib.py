"""Basic arithmetic operations on integers."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def divide(a: int, b: int) -> tuple[int, int]:
    """Return the division of two integers."""
    if b == 0:
        msg = f"Cannot divide {a} by zero."
        raise ValueError(msg)
    return a // b, a % b
