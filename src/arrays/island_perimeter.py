def in_bounds(A, pos):
    if pos[0] < 0 or pos[0] > len(A) - 1:
        return False
    if pos[1] < 0 or pos[1] > len(A[0]) - 1:
        return False
    return True

def get_perimeter(A):
    if not A or not A[0]:
        return 0
    m, n, p = len(A), len(A[0]), 0
    dpos = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(n):
        for j in range(m):
            if not A[i][j]:
                continue
            for di, dj in dpos:
                if not in_bounds(A, (i + di, j + dj)) or not A[i + di][j + dj]:
                    p += 1
    return p
