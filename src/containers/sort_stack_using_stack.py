def sort(stack):
    stack1 = list(stack)
    stack2 = []
    while stack1:
        x = stack1.pop()
        while stack2 and stack2[-1] > x:
            stack1.append(stack2.pop())
        stack2.append(x)
    return stack2
