"""Function find to perform the binary search
"""
def find(search_list, value):
    
    """Find the index of the value in a sorted list.

    Args:
        search_list (list[int]): The sorted list.
        value (int): The int value to search for.

    Returns:
        int: The index of the value in the search list.

    Raises:
        TypeError: If search_list or value has an invalid type.
        ValueError: if value isn't found.
    """

    if not isinstance(search_list, list):
        raise TypeError("search_list must be a list")
    if not all(isinstance(element, int) and not isinstance(element, bool)for element in search_list):
        raise TypeError("search_list must contain only integers")
    if not isinstance(value, int):
        raise TypeError("Value must be an integer")
    
    low = 0
    high = len(search_list) -1 
    
    # repeatedly search for an element
    # while doing so, decrease your domain of search.
    while low <= high:
        
        mid_index = low + (high - low)//2
            
        if search_list[mid_index] == value:
            return mid_index
        elif search_list[mid_index] < value:
            low = mid_index + 1
        else:
            high = mid_index - 1
    
    #if not found 
    raise ValueError("value not in array")
