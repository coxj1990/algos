class Queue:

    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        return self.q.pop(0)

    def empty(self):
        return len(self.q) == 0
