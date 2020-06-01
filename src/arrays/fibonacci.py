def fib_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_memo(n, memo={}):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in memo:
        return memo[n]
    res = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = res
    return res

def fib_dp(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    dp = [0, 1]
    for _ in range(2, n):
        dp.append(dp[-1] + dp[-2])
    return dp[-1]
