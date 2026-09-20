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
    flag = 1
    if number % 3 == 0 :
        result += "Pling"
        flag = 0
    if number % 5 == 0:
        result += "Plang"
        flag = 0
    if number % 7 == 0:
        result += "Plong"
        flag = 0
    if flag:
        result += str(number)

    return result