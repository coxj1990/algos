def evaluate(stack):
    res = stack.pop() if stack else 0
    while stack and stack[-1] != ')':
        op = stack.pop()
        if op == '+':
            res += stack.pop()
        else:
            res -= stack.pop()
    return res

def calculate(expr):
    stack = []
    for i in range(len(expr) - 1, -1, -1):
        e = expr[i]
        if e == ' ':
            continue
        elif e == ')' or e == '+' or e == '-':
            stack.append(e)
        elif e.isdigit():
            n = e
            while i > 0 and expr[i - 1].isdigit():
                i -= 1
                n = expr[i] + e
            stack.append(int(n))
        else:  # e == '('
            res = evaluate(stack)
            stack.pop()
            stack.append(res)
    return evaluate(stack)
