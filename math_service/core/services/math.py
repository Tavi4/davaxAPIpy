from functools import lru_cache


@lru_cache(maxsize=128)
def calculate_power(base: float, exponent: float) -> float:
    if base == 0 and exponent < 0:
        raise ValueError("0 cannot be raised to a negative power.")
    return base ** exponent


@lru_cache(maxsize=128)
def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@lru_cache(maxsize=128)
def calculate_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return a
