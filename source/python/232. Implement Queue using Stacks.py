class MyQueue:

    def __init__(self):
        self.input: list[int] = []
        self.output: list[int] = []

    def push(self, x: int) -> None:
        while self.output:
            self.input.append(self.output.pop())
        self.input.append(x)

    def pop(self) -> int:
        while self.input:
            self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        while self.input:
            self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
if __name__ == "__main__":
    queue = MyQueue()

    assert queue.empty() == True

    queue.push(1)
    queue.push(2)

    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() == False

    print("All tests passed!")
