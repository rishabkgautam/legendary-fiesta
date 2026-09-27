"""Function to reverse a string
    
    First approach
    --------------
    # using temp as a temporary var, C style
    
    list_of_char = list(text)
    
    for index in range(len(text)//2):
        temp = list_of_char[index]
        list_of_char[index] = list_of_char[-index-1]
        list_of_char[-index-1] = temp

    return "".join(list_of_char)

    Second approach
    ---------------
    # Using tuple unpacking
    
    list_of_char = list(text)
    
    for index in range(len(text)//2):
        list_of_char[index], list_of_char[-index-1] = list_of_char[-index-1], list_of_char[index]

    return ''.join(list_of_char)
    
"""

def reverse(text):
    """Uses the python string slicing to reverse a string

    Args:
        text (str): str to be reversed

    Returns:
        str : The reversed string.
    
    """
    
    return text[::-1]