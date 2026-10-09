"""Function to compute the value of color coded resistor"""

color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    """Compute the integer values of the first two color strip.

    Args:
        colors (list[str]): The list of color sequence on resistor.

    Returns:
        int : The 2 digit decimal value corresponding to first two color strips.
    """
    
    return int(
        "".join(map(str, [color_list.index(colors[0])]
        + [color_list.index(colors[1])]))
    )
