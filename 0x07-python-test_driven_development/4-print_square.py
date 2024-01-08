#!/usr/bin/python3
def print_square(size):
    """Function to print square
    Args:
        size: Length of the square
    Raises:
        TypeError: If not an integer
        ValueError: if size is less than zero
        TypeError: If not a float
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size,  float) and size <= 0:
        raise TypeError("size must be >= 0")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end="")
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
