class MinStack:
    def __init__(self) -> None:
        self.myStack = []
        self.minStack = []

    def push(self, val):
        self.myStack.append(val)
        minVal = min(val, self.getMin() if self.getMin() else val)
        self.minStack.append(minVal)
    
    def pop(self):
        self.myStack.pop()
        self.minStack.pop()

    def top(self):
        return self.myStack[-1]

    def getMin(self):
        return self.minStack[-1]
