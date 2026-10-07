"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def contains(smaller, larger):
    """Check if smaller list is actually smaller than larger or not

    Args:
        smaller (list[int]): The smaller list.
        larger (list[int]): The larger list.

    Returns: 
        bool : True when smaller list is smaller than larger else False.
    """
    size = len(smaller)

    for i in range(len(larger) - size + 1):
        if larger[i:i + size] == smaller:
            return True

    return False


def sublist(list_one, list_two):
    """Return the relation between list_one and list_two from {EQUAL, SUBLIST, SUPERLIST, UNEQUAL}.

    Args:
        list_one (list[int]): The first list.
        list_two (list[int]): The second list.

    Returns:
        str : The sublist category. 
    """
    if list_one == list_two:
        return EQUAL

    if contains(list_one, list_two):
        return SUBLIST

    if contains(list_two, list_one):
        return SUPERLIST

    return UNEQUAL
    
    
    
        
            
