def num_subarrays_with_odd_sum(L):
    n = len(L)
    even = [0] * n
    odd = [0] * n
    for i in range(n):
        is_even = L[i] % 2 == 0
        if i == 0:
            even[i] = is_even
            odd[i] = not is_even
        else:
            if is_even:
                even[i] = even[i - 1] + 1
                odd[i] = odd[i - 1]
            else:
                even[i] = odd[i - 1]
                odd[i] = even[i - 1] + 1
    return sum(odd)
