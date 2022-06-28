#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """prints square with size
    checks if "size is an int, a float and less than 0,
    size is less than 0 or size is equal to 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        return None

    for row in range(size):
        print('#' * size)
