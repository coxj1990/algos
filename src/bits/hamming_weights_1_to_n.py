def hamming_weights(n):
    weights = [0]
    for i in range(1, n + 1):
        weights.append(weights[i & (i - 1)] + 1)
    return weights
