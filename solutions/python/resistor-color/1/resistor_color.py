"""Function to return all the colors and the value associated with a resistor strip color."""

color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def color_code(color):
    """Computes the value of a color strip.
    
    Args:
        color (str): The color of resistor strip.
    
    Returns:
        int : The value associated with a resistor line.
    """
    return color_list.index(color)


def colors():
    """Returns all the colors of the resistor strips
    """
    return color_list
