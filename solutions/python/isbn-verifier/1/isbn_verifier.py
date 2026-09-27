"""Function to check if the given isbn string is a valid ISBN-10
"""

def is_valid(isbn):
    """Check if isbn is a valid ISBN-10

    Args:
        isbn (str): the string to check for ISBN-10

    Returns:
        bool: True if it is a ISBN-10, false otherwise
    """

    # drop the dashes
    isbn = isbn.replace("-", "")

    # check if the first 9 chars are actually digit and the isbn has length 10
    if len(isbn) != 10 or not all(ch.isdecimal() for ch in isbn[:-1]) :
        return False
        
    # find sum of the first 9 digit times thier rank 10-2
    result = sum(rank * int(ch) for ch, rank in zip(isbn[:-1], range(10,1,-1)))
    
    #if it's a X add 10, otherwise add the number to the sum
    last_ch = isbn[-1]
    if last_ch == "X":
        result += 10
    elif last_ch.isdecimal():
        result += int(last_ch)
    else:
        return False
    
    return result % 11 == 0

