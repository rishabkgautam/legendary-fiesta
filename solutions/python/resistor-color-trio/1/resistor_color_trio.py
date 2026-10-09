"""Function to compute the resistance from the color coding of a resistor with apt
metric prefix."""

color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def label(colors):
    """Calculate the resistance from the colors list and append the correct metric.

    Args:
        colors (list[str]): List of first three strip colors of the resistor. 

    Returns:
        str : The resistance value
    """
    digits = str(
        color_list.index(colors[0]) * 10 + color_list.index(colors[1])
    )

    multiplier_exp = color_list.index(colors[2])
    
    #append zeros according to the multiplier value
    digits += "0" * multiplier_exp
    
    zeros_count = len(digits) - len(digits.rstrip("0"))
    trailing_zeros = zeros_count % 3
    
    prefixes = [" ", " kilo", " mega", " giga"]
    prefix = prefixes[min(zeros_count // 3, 3)]

    return f"{digits.strip("0") + "0" * trailing_zeros + prefix}ohms"

    