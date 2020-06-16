def get_primes(n):
    is_prime = [True for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]
