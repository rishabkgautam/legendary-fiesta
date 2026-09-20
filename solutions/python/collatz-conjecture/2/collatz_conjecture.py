"""The Collatz conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.

If the number is even, divide it by 2. If it is odd, multiply it by 3 and add 1. Repeat until the number reaches 1.
"""


def steps(number):
    """Calculates the number of steps required for a number to reach 1.

    Args:
        number (int): The number to check against the Collatz conjecture.

    Returns:
        int: The number of steps it takes for the number to reach 1.

    Raises:
        ValueError: If the number is not a positive integer.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step_count = 0

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        step_count += 1

    return step_count
