"""Function to apply rotations to the letters of a plaintext.
"""

def rotate(text, key):
    """rotate each letter by key

    Args:
        text (str): The plaintext
        key (int): By what rotation to shift each letter

    Returns:
        str: The rotated cipher text.
    """
    
    lst = []
    base = 0
    for letter in text:
        if not letter.isalpha():
            lst.append(letter)
            continue
            
        base = ord('A') if letter.isupper() else ord('a')         
        lst.append(chr((ord(letter) - base + key) % 26 + base))

    return ''.join(lst)
        
