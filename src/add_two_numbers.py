def add(x, y):
    res = x ^ y
    carry = (x & y) << 1
    while carry:
        res_cpy = res
        res ^= carry
        carry = (res_cpy & carry) << 1
    return res
