def reverse(x):
    res = 0
    while x:
        res <<= 1
        res += (x & 1)
        x >>= 1
    return res
