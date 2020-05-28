def hamming_weight(x):
    weight = 0
    while x:
        x &= (x - 1)
        weight += 1
    return weight
