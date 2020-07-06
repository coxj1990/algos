def lis(L):
    n = len(L)
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if L[j] < L[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if dp else 0
