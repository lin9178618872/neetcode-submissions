class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是长度较小的，提升二分效率
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m  # 只在 nums1 上二分

        while left <= right:
            i = (left + right) // 2
            j = half - i

            # 边界处理：如果越界，用 ±inf 替代
            nums1_left = nums1[i-1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')

            # 满足条件的分割点
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # 奇数总长 → 返回右边最小
                if total % 2 == 1:
                    return min(nums1_right, nums2_right)
                # 偶数总长 → 左最大 + 右最小
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

            # 调整二分方向
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1
