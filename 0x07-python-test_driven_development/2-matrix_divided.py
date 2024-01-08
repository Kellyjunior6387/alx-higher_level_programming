def matrix_divided(matrix, div):
    """ Function to divide all elements in a matrix
    Args:
        matrix: the matrix to be divided
        div: the divisor
    Return:
        lists: Matrix of quotients
    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of" + 
        "integers/floats")
    for row in matrix:
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)" +
            "of integers/floats")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                "integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]
