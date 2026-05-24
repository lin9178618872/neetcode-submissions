from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # 保证 nums1 是短数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total = m + n
        half = total // 2

        left = 0
        right = m

        while left <= right:

            # i 是 nums1 的切割位置
            i = left + (right - left) // 2

            # j 是 nums2 的切割位置
            j = half - i

            # nums1 左边最大值
            if i > 0:
                nums1_left = nums1[i - 1]#左边最后一个元素位置，即系切割线左边的最后一个
            else:
                nums1_left = float("-inf")

            # nums1 右边最小值
            if i < m:
                nums1_right = nums1[i]
            else:
                nums1_right = float("inf")

            # nums2 左边最大值
            if j > 0:
                nums2_left = nums2[j - 1]
            else:
                nums2_left = float("-inf")

            # nums2 右边最小值
            if j < n:
                nums2_right = nums2[j]
            else:
                nums2_right = float("inf")

            # 找到正确切割，-inf<=+inf
            if nums1_left <= nums2_right and nums2_left <= nums1_right:

                # 奇数
                if total % 2 == 1:
                    return min(nums1_right, nums2_right)

                # 偶数
                left_max = max(nums1_left, nums2_left)
                right_min = min(nums1_right, nums2_right)

                return (left_max + right_min) / 2

            # nums1 左边太大，减一位
            elif nums1_left > nums2_right:
                right = i - 1

            # nums2 左边太大，加一位
            else:
                left = i + 1

