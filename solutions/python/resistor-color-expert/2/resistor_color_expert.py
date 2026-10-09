"""Function to compute the resistance of a resistor using their band colors
"""

color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

tolerance_list = { "grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10}

def resistor_label(colors):

    """Calculate the resistance from the colors list and append the correct metric and tolerance.

    Args:
        colors (list[str]): List of color bands of the resistor. 

    Returns:
        str : The resistance value
    """

    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"
    
    digits = color_list.index(colors[0]) * 10 + color_list.index(colors[1])

    if len(colors) == 5:
        digits = digits * 10 + color_list.index(colors[2])

    multiplier_exp = color_list.index(colors[-2])
    
    resistance = digits * 10 ** multiplier_exp
    
    prefixes = ["", "kilo", "mega", "giga"]
    prefix_index = 0

    while resistance >= 1000 and prefix_index < len(prefixes) -1:
        resistance /= 1000
        prefix_index += 1
         
    tolerance = tolerance_list[colors[-1]]

    return f"{int(resistance) if resistance.is_integer() else resistance} {prefixes[prefix_index]}ohms ±{tolerance}%"
