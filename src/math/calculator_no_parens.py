def calculate(s):
    if not s:
        return 0
    res, curr = 0, int(s[0])
    for i in range(1, len(s), 2):
        op, num = s[i], int(s[i + 1])
        if op == '+':
            res += curr
            curr = num
        elif op == '-':
            res += curr
            curr = -num
        elif op == '*':
            curr *= num
        elif op == '/':
            curr /= int(num)
    return res + curr
