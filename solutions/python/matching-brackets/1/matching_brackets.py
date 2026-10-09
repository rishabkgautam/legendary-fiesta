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

    for ch in input_string:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return not stack
    
    return len(brackets) == 0
        
