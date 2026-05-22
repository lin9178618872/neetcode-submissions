class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        
        # 存放答案
        res = [0] * n
        
        # 单调栈，存下标
        s = []
        
        # 从右往左遍历
        for i in range(n - 1, -1, -1):
            
            # 把右边不比自己大的都弹掉
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            
            # 栈顶就是右边第一个更大的温度
            if not s:
                res[i] = 0
            else:
                res[i] = s[-1] - i
            
            # 当前下标入栈
            s.append(i)
        
        return res