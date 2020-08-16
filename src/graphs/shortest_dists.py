# Bellman-Ford algorithm
# O(mn) time
# O(n) space
# Works for non-negative edge costs, unlike Dijstra
# if dp[n-1] != dp, a negative cost cycle exists

def shortest(G, start):
    n = len(G)
    dp = [float('inf') if i != start else 0 for i in range(n)]
    for i in range(1, n):
        dp_new = list(dp)
        for w in range(n):
            for v, cost in G[w]:
                dp_new[v] = min(dp_new[v], dp[w] + cost)
        dp = dp_new
    return dp
