class Stack:

    def __init__(self):
        self.s = []
        self.maxes = []

    def push(self, x):
        self.s.append(x)
        if not self.maxes:
            self.maxes.append(x)
        else:
            self.maxes.append(max(x, self.maxes[-1]))

    def pop(self):
        self.maxes.pop()
        return self.s.pop()

    def max(self):
        return self.maxes[-1]
