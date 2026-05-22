from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        不返回任何东西，直接在 nums1 里完成合并
        """

        # last 指向 nums1 最后一个可以放元素的位置
        last = m + n - 1

        # 从后往前比较，把大的放到 last 位置
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # 如果 nums2 还有剩余元素，继续放进 nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
