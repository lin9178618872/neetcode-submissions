from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()     # 存索引，保持单调递减
        res = []

        left, right = 0, 0
        while right < len(nums):
            # c 是将移入窗口的元素索引
            c = right

            # window.add(c)
            # 👉 把所有比 nums[c] 小的从队尾移除
            while window and nums[window[-1]] <= nums[c]:
                window.pop()
            window.append(c)

            # 增大窗口
            right += 1

            # 判断左侧窗口是否要收缩（窗口大小 > k）
            while right - left > k:
                d = left
                # window.remove(d)
                if window and window[0] == d:
                    window.popleft()
                left += 1

            # 当窗口大小 == k，记录答案
            if right - left == k:
                res.append(nums[window[0]])

        return res
