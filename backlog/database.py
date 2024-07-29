
class Backlog:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        return self.stack

    def pop(self):
        self.stack.pop()
        return self.stack

    def peek(self):
        return self.stack[-1]

    def show(self):
        return self.stack
