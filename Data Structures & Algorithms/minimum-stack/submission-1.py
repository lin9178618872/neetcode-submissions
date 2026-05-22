class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
    # 先放进普通栈
        self.stack.append(val)

    # 如果最小栈是空的（第一次放数）
        if not self.minStack:
        # 那当前最小值就是 val 自己
            self.minStack.append(val)
        else:
        # 如果最小栈不是空的
        # 取 现在的值 和 之前最小值 比较
            current_min = self.minStack[-1]

        # 谁小就存谁
            if val < current_min:
                self.minStack.append(val)
            else:
                self.minStack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]