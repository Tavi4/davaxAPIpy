def calculate_pow(a: int, b: int) -> int:
    """Computes a^b."""
    return a ** b


def calculate_factorial(n: int) -> int:
    """Computes factorial of n (n!)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def calculate_fibonacci(n: int) -> int:
    """Computes the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
