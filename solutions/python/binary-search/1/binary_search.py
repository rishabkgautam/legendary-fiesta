"""Function find to peform the binary search
"""
def find(search_list, value):
    
    """Find the index of the element value else return an error.

    Args:
        search_list (list[int]): The list to search in for the element.
        value (int): The int value to search for.

    Returns:
        int: The index of the value element.

    Raises:
        ValueError: if value isn't found.
    """

    if not all(isinstance(element, int) for element in search_list):
        return 
        
    # perform binary search
    search_list.sort()
    low = 0
    high = len(search_list) -1 
    
    # repeatedly search for an element
    # while doing so, decrease your domain of search.
    
    while ( low <= high):
        
        mid_index = low + (high - low)//2
            
        if search_list[mid_index] == value:
            return mid_index
        elif search_list[mid_index] < value:
            low = mid_index + 1
        elif search_list[mid_index] > value:
            high = mid_index - 1

    
    #if not found 
    raise ValueError("value not in array")
