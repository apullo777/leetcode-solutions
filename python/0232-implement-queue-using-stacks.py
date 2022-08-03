# https://leetcode.com/problems/implement-queue-using-stacks/

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

class MyQueue:

    def __init__(self):
        self.inStack, self.outStack = [], []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.move()
        return self.outStack.pop()

    def peek(self) -> int:
        self.move()
        return self.outStack[-1]

    def empty(self) -> bool:
        return (not self.inStack) and (not self.outStack)
    
    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())  

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()