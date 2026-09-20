"""
Bob's response logic.

Context:
Bob is a lackadaisical boy who replies with short, limited answers.
Try talking to him!
"""

def response(hey_bob: str) -> str:
    """
    Generate Bob's response to user input.

    Args:
        hey_bob (str): The user's message.

    Returns:
        str: Bob's reply.
    """
    text = hey_bob.strip()

    if not text:
        # Empty input or only whitespace
        return "Fine. Be that way!"

    is_question = text.endswith("?")
    is_shouting = hey_bob.isupper() and any(char.isalpha() for char in hey_bob)

    if is_shouting and is_question:
        # Shouted question
        return "Calm down, I know what I'm doing!"
    elif is_question:
        # Normal question
        return "Sure."
    elif is_shouting:
        # Shouting (not a question)
        return "Whoa, chill out!"
    else:
        # Default response
        return "Whatever."
