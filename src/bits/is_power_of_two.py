def is_power_of_two(x):
    return (x > 1) and (x & (x - 1)) == 0
