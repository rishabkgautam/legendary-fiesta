""" Function to check if a sentence is a pangram (a sentence containing all the a-z or A-Z letters). 
"""

def is_pangram(sentence):
    """ Check if sentence is pangram

    Args:
        sentence (str) : The sentence to check

    Returns:
        bool : True if it is a pangram, False otherwise
    """
    
    new_sentence = ''.join([letter for letter in sentence if letter.isalpha()])
    return len(set(new_sentence.lower())) == 26 
