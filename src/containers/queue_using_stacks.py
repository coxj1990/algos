from src.containers.stack_push_pop import Stack

class Queue:

    def __init__(self):
        self.s1 = Stack()

    def push(self, x):
        self.s1.push(x)

    def pop(self):
        s2 = Stack()
        while not self.s1.empty():
            s2.push(self.s1.pop())
        x = s2.pop()
        while not s2.empty():
            self.s1.push(s2.pop())
        return x
