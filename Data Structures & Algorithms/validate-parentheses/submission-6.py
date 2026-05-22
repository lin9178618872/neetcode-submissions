class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in mapping:  # 右括号
                if stack:
                    top = stack.pop()
                else:
                    top = '#'

                if mapping[c] != top:
                    return False
            else:
                stack.append(c)

        return not stack
