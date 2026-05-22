class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # 结果数组，先全部填 0
        # 代表：默认以后都没有更热的天
        res = []
        for i in temperatures:
            res.append(0)

        # 栈：专门存还没遇到更热天气的“天的下标”
        stack = []

        # 一个一个天去看
        for i in range(len(temperatures)):

            # 今天的温度
            current_temp = temperatures[i]

            # 如果栈不空，并且今天比栈顶那天更热
            while stack and current_temp > temperatures[stack[-1]]:

                # 取出栈顶那一天
                prev_index = stack.pop()

                # 算距离：今天 - 那一天
                res[prev_index] = i - prev_index

            # 把今天放进栈（等以后更热的天）
            stack.append(i)

        return res
