class MyQueue:
    def __init__(self):
        self.stack1 = []  # Main stack for push operations
        self.stack2 = []  # Temporary stack for reverse operations

    def push(self, x: int) -> None:
        self.stack1.append(x)  # Push directly to stack1

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2