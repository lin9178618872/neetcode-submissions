from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []

        left, right = 0, 0
        while right < len(nums):
            c = right

            while window and nums[window[-1]] <= nums[c]:
                window.pop()
            window.append(c)

            right += 1

            while right - left > k:
                d = left
                if window and window[0] == d:
                    window.popleft()
                left += 1

            if right - left == k:
                res.append(nums[window[0]])

        return res
