"""Function to check for phrase being a isogram (phrase with no repeating letters)
"""

def is_isogram(phrase):
    """ Check if phrase is isogram

    Args:
        phrase (str): The string to check

    Returns:
        bool : True if it's a isogram, False otherwise
        
    return len(set(letter for letter in phrase.lower() if letter.isalpha())) == sum(int(letter.isalpha()) for letter in phrase.lower())
    """
    
    letters = [char.lower() for char in phrase if char.isalpha()]
    return len(letters) == len(set(letters))