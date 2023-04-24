class Stack:
    def __init__(self):
        self.stack = []

    def top(self) -> int:
        if not self.isEmpty:
            return self.stack[-1]
        
    def push(self, x: int):
        self.stack.append(x)

    def pop(self) -> int:
        if not self.isEmpty:
            return self.stack.pop()
        
    def isEmpty(self) -> bool:
        return len(self.stack) > 0

