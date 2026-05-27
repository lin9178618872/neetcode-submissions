class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in mapping:  # 右括号
                if stack:#如果栈不为空就踢出来
                    top = stack.pop()
                else:
                    top = '#'

                if mapping[c] != top:#相对的不一样就返回错误
                    return False
            else:
                stack.append(c)

        return not stack
