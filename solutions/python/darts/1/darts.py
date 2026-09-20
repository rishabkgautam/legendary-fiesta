"""Function to calculate the euclidean distance of the point from the origin and rewarding points accordingly.
"""

def score(x, y):
    """Checks the distance and produce a numeric score from 0, 1, 5, 10

    Args:
        x, y (float): The coordinates of the given point

    Returns:
        int : The numeric score it achieves.
    """
    dist = (x ** 2 + y ** 2) ** 0.5

    if dist <= 1:
        return 10
    elif dist <= 5:
        return 5
    elif dist <= 10:
        return 1
    else:
        return 0
