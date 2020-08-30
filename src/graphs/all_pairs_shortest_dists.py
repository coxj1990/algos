def shortest(G):
    n = len(G)
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0
            elif i in G and j in G[i]:
                dp[i][j] = G[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp
