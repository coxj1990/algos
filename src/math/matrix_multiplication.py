def matmul(A, B):
    m, p, n = len(A), len(A[0]), len(B[0])
    C = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][k] += A[i][j] * B[j][k]
    return C
