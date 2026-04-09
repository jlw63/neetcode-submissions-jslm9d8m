class MinStack:
    def __init__(self):
        self.stack = []
        self.min_so_far = None

    def push(self, val: int) -> None:
        #if stack empty
        if not self.stack:
            min_so_far = val
        if self.stack: #stack has values
            min_so_far = self.stack[-1][1]
            min_so_far = min(min_so_far, val)
        value = [val, min_so_far]
        self.stack.append(value)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
