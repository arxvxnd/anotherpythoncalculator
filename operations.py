def add_operation(a: float, b: float) -> float:
    """
    Returns the sum of two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


def subtract_operation(a: float, b: float) -> float:
    """
    Returns the difference between two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of a minus b.
    """
    return a - b


def multiply_operation(a: float, b: float) -> float:
    """
    Returns the product of two numbers.

    Parameters:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    return a * b


def division_operation(a: float, b: float) -> float:
    """
    Returns the quotient of two numbers.

    Parameters:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def modulus_operation(a: float, b: float) -> float:
    """
    Returns the remainder of dividing a by b.
    """
    return a % b


def power_operation(a: float, b: float) -> float:
    """
    Returns a raised to the power of b.
    """
    return a ** b


def square_root_operation(a: float) -> float:
    """
    Returns the square root of a number.
    If a is negative, prints an error message and returns None.
    """
    if a < 0:
        print("Error: Cannot take square root of a negative number.")
        return None
    return a ** 0.5


def factorial_operation(n: int) -> int:
    """
    Returns the factorial of n.
    If n is negative, prints an error message and returns None.
    """
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def absolute_value_operation(a: float) -> float:
    """
    Returns the absolute value of a number.
    """
    return abs(a)


def percentage_operation(part: float, whole: float) -> float:
    """
    Returns the percentage of part relative to whole.
    """
    if whole == 0:
        print("Error: Cannot calculate percentage with a whole of zero.")
        return None
    return (part / whole) * 100