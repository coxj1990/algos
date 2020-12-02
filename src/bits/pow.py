from __future__ import division

# Computes x^n
# O(logn)

def pow_pos(x, n):
    res = 1
    while n:
        if (n & 1):
            res *= x
        n >>= 1
        x *= x
    return res

def pow(x, n):
    return 1 / pow_pos(x, -n) if n < 0 else pow_pos(x, n)
