def bitwise_and_range(n, m):
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1
    return m << i
