"""Function to classify a number as perfect, abundant, or deficient based on its aliquot sum."""

def classify(number):
    """A perfect number equals the sum of its positive divisors.

    Args:
        number (int): A positive integer

    Returns:
        str: The classification of the input integer ('perfect', 'abundant', or 'deficient')

    Raises:
        ValueError: If number is not a positive integer
    """
    
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1 : return "deficient"
    
    # Calculate aliquot sum (sum of proper divisors)
    aliquot_sum = 0
    for index in range(1, int(number ** 0.5) + 1):
        if number % index == 0:
            aliquot_sum += index
            if index != 1 and index ** 2 != number:
                aliquot_sum += number // index

    # classify based on comparison
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"
    
        
