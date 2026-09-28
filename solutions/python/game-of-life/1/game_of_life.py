"""Function to generate the next state for the Conway's Game of Life
"""

def tick(matrix):
    """
    Calculate the the new values for the next state from the old state matrix

    Args:
        matrix (list[list[int]]): A 2D list of integers (0 or 1).

    Returns: 
        list[list[int]]: The next state matrix, or None if invalid input.
    """
    
    matrix_order = len(matrix)
    next_state = [[0] * matrix_order for _ in range(matrix_order)]

    # Proceed only if it's a square matrix with int elements
    for rows in matrix:
        if (
            not isinstance(rows, list)
            or len(rows) != matrix_order
            or not all(
                isinstance(element, int) 
                and element in [0,1] 
                for element in rows
            )
        ):
            return

    # if an empty matrix is given as input then an empty matrix would be returned.

    # lists to help in finding the sum of values in adjacent squares
    x_adjacents = [-1, 1, 0]
    y_adjacents = [-1, 1, 0]

    current_adj_squares_sum = 0
    
    # adjacent squares sum 
    
    for matrix_y in range(matrix_order):
        for matrix_x in range(matrix_order):
            current_adj_squares_sum = sum(
                matrix[matrix_y + lever_y][matrix_x + lever_x]
                for lever_y in y_adjacents
                for lever_x in x_adjacents
                if 0 <= matrix_x + lever_x < matrix_order
                and 0 <= matrix_y + lever_y < matrix_order
                and not (lever_x == 0 and lever_y == 0)
            )

            # compute the next state
            # check each cell or element for three conditions

            # if 3 adjacents are 1: new element is 1
            
            if current_adj_squares_sum == 3:
                next_state[matrix_y][matrix_x] = 1

            # if 2 adjacents are 1 copy the old value
            elif current_adj_squares_sum == 2:
                next_state[matrix_y][matrix_x] = matrix[matrix_y][matrix_x]

            # else new element value is 0 
            else: 
                next_state[matrix_y][matrix_x] = 0

    return next_state
       
    
