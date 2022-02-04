class MyQueue:
    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        # O(n)
        stack2 = []
        while not self.empty():
            stack2.append(self.pop())
        stack2.append(x)
        while stack2:
            self.stack.append(stack2.pop())
        

    def pop(self) -> int:
        if self.empty():
            return None
        return self.stack.pop()
        

    def peek(self) -> int:
        if self.empty():
            return None
        return self.stack[-1]
        

    def empty(self) -> bool:
        return self.stack == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()