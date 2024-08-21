
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.minstack) == 0):
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

input = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
expect = [None     , None     , None     , None     , 0       , None , 2    , 1]

