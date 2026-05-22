class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # 用一个栈（列表）来存数字
        stack = []

        # 一个一个读取 tokens 里的内容
        for c in tokens:

            # 如果是加号 +
            if c == "+":

                # 先弹出栈顶的数字
                num1 = stack.pop()

                # 再弹出下一个数字
                num2 = stack.pop()

                # 把两个数字相加
                result = num2 + num1

                # 把结果放回栈里
                stack.append(result)

            # 如果是减号 -
            elif c == "-":

                num1 = stack.pop()   # 后出来的
                num2 = stack.pop()   # 先出来的

                result = num2 - num1

                stack.append(result)

            # 如果是乘号 *
            elif c == "*":

                num1 = stack.pop()
                num2 = stack.pop()

                result = num2 * num1

                stack.append(result)

            # 如果是除号 /
            elif c == "/":

                num1 = stack.pop()
                num2 = stack.pop()

                # 先除，再转成整数（题目要求向0取整）
                result = int(num2 / num1)

                stack.append(result)

            # 如果是数字
            else:

                # 把字符串变成整数
                number = int(c)

                # 放进栈里
                stack.append(number)

        # 最后栈里只剩一个数，就是答案
        return stack[0]
