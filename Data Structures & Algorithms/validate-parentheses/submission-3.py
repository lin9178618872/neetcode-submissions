class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:  # 右括号
                if stack:
                    top = stack.pop()
                else:
                    top = '#'

                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
