class Stack:

    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        return self.q.pop()
