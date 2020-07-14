def rotate(A):
    n = len(A)
    # transpose
    for i in range(n):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    # reverse columns
    for row in A:
        for i in range(n // 2):
            row[i], row[n - i - 1] = row[n - i - 1], row[i]
