"""Function to rebase a number given as digits list
"""

import math

def rebase(input_base, digits, output_base):
    """rebase the given number and produce the output number

    Args:
        input_base (int): The input base number
        digits (list[int]): List containing the digits of given number
        output_base (int): The output_base number

    Returns:
        list[int]: List of digits in the rebased number.
    """
    
    if input_base < 2 : 
        raise ValueError("input base must be >= 2")
        
    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    if not all( 0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if digits == [] or all(digit == 0 for digit in digits):
        return [0]
    
    decimal_number = sum ( value * input_base ** index for index, value in enumerate(reversed(digits)))
    
    result = []
    
    current_num = decimal_number

    # max_power = floor (log input_base of that number)
    
    max_power = math.floor(math.log(decimal_number, output_base))
    
    current_exp = max_power
    
    
    while current_exp != -1: 
    
        coeff = current_num // output_base ** current_exp
        
        result += [coeff]
        
        current_num -= coeff * output_base ** current_exp
             
        current_exp -= 1
        
    return result
