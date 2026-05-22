class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # 左括号 -> 右括号
        mapping = {'(': ')', '[': ']', '{': '}'}
        
        for char in s:
            
            if char in mapping:
                # 如果是左括号
                stack.append(char)
            
            else:
                # 如果是右括号
                
                if not stack:
                    # 没有左括号可以匹配
                    return False
                
                top = stack.pop()
                # 拿出最近的左括号
                
                if mapping[top] != char:
                    # 看这个左括号对应的右括号
                    # 和当前右括号是不是一样
                    return False
        
        # 最后如果栈空，说明全部匹配
        return not stack
