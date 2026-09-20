"""Function to convert number to raindrop sounds based its divisibility by 3,5 or 7.
"""

def convert(number):
    """Converts number to their corresponding rain drop sound.

    Args:
        number(int): The input number
        
    Returns:
        str: Returns different sounds (e.g. Pling).
    """
    result = ""
    if number % 3 == 0 :
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if not result:
        result += str(number)

    return result