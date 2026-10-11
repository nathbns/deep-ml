def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    ans = []
    if a is not None:
        n = len(a[0])
        m = len(a)

    for i in range(n):
        new_row = []
        for j in range(m):
            new_row.append(a[j][i])
        ans.append(new_row)

    return ans