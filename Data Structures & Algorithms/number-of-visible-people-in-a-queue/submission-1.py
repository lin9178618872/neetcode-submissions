class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < heights[i]:#当有栈的时候跟栈顶小高度大
                stack.pop()#栈拔出
                res[i] += 1#结果+1

            if stack:#栈还有
                res[i] += 1#结果+1
            stack.append(heights[i])#把高度加进去栈如果没有元素

        return res
        