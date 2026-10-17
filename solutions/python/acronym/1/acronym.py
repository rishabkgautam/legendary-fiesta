"""Function to create abbreviations of different combinations of words"""

def abbreviate(words):
    """Pick the first letters (upper-case) of each word while dropping any _,- etc
    
    Args:
        words (str): A sequence of words.
        
    Returns:
        str : The generated acronym.
    """
    
    acronym = []
    for word in words.replace('-',' ').replace('_',' ').split():
        acronym.append(word[0])

    return ''.join(acronym).upper()
    
