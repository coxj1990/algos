def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x
