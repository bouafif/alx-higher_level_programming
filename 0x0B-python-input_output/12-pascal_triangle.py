#!/usr/bin/python3
"""Create a function def pascal_triangle(n)"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the n-th row and return it as a list
    of lists of integers.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []  # Return an empty list if n <= 0

    # Initialize Pascal's triangle with the first two rows
    triangle = [[1], [1, 1]]

    # Generate subsequent rows of Pascal's triangle
    for i in range(2, n):
        prev_row = triangle[-1]  # Get the last row
        new_row = [1]  # Start with 1 as the first element

        # Compute the values in the row based on the previous row
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])
        new_row.append(1)  # End with 1 as the last element

        triangle.append(new_row)  # Append the new row to the triangle

    return triangle
