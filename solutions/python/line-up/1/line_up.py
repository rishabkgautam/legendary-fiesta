"""Function to return a welcoming remark for lined up customers
"""
def line_up(name, number):
    """Craft a remark based on the customer name and the nth customer number they're serving today.  

    Args:
        name (str): The customer's name
        number (int): The number of customer they're visting their shop

    Returns:
        str : A sentence stating a customer that you're the nth customer on their shop today with a thank you at the end.
    
    """
    
    suffix = ''

    if number % 10 == 1 and number % 100 != 11: 
        suffix = 'st'
    elif number % 10 == 2 and number % 100 != 12:
        suffix = 'nd'
    elif number % 10 == 3 and number % 100 != 13:
        suffix = 'rd'
    else: 
        suffix = 'th'

    return name + ', you are the ' + str(number) + suffix + ' customer we serve today. Thank you!'
