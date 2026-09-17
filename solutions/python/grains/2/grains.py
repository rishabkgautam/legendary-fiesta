""" functions to calculate number of grains on a square and total grains being used. The square function raises a ValueError if number is not between 1 and 64
"""

def square(number):
    """Calculate the number of grains on a square based on the number provide.

    Args:
        number(int): The number of square on the board.

    Returns:
        int: The number of grains on that particular square

    Raises: 
        ValueError: if number is less than 1 or greater than 64.
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)

def total():
    """Calculate the total number of grains on the chessboard.
    
    Returns:
        The total number of the grains spread across the board.    
    """
    return 2 ** 64 - 1
