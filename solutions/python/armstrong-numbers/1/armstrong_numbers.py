""" Function to tell if a number is an Armstrong number.
"""
def is_armstrong_number(number):
    """Checks if the given number is a Armstrong number.

    Args:
        number(int): number to check.

    Returns:
        bool: True if it's a Armstrong number, False otherwise.
    """
    n = len(str(number))
    s = sum((int(x)) ** n for x in str(number))
    if s == number:
        return True
    return False
