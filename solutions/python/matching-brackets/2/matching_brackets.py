"""Function to verify all the brackets, braces and parentheses are matched."""

def is_paired(input_string):
    """Verify that all pairs among (), {}, [] are matched.

    Args:
        input_string (str): The input string.

    Returns:
        bool: True if all pairs are match, False otherwise.
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for character in input_string:
        if character in '([{':
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False

    return not stack
    
        
