"""The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.

The operations include the continuous division of the number by 2 if it's even and if it's odd we'll multipy by 3 and then add 1 to make it even and proceed until the number reaches 1.
"""

def steps(number):
    """Calculates the number of steps required for a number to find its way to 1.    
    
    Args:
        number(int): The number to check against the collatz conjecture

    Returns:
        int: The number of steps it takes for the number to reach 1.
    """
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    step_count = 0
    
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            step_count += 1
        else:
            number = number * 3 + 1
            step_count += 1

    return step_count