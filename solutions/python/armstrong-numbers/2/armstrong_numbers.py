""" Function to tell if a number is an Armstrong number.
"""
def is_armstrong_number(number):
    """Checks if the given number is a Armstrong number.

    Args:
        number(int): number to check.

    Returns:
        bool: True if it's a Armstrong number, False otherwise.
    """
    number_of_digits = len(str(number))
    sum_of_the_nth_power_of_the_digits = sum((int(x)) ** number_of_digits for x in str(number))
    
    if sum_of_the_nth_power_of_the_digits == number:
        return True
    return False
