from typing import List

class Solution:
    # 在旋转排序数组中搜索目标元素 target 的索引，若不存在则返回 -1
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        # right 始终指向数组的最后一个元素索引
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            # 1. 找到目标，直接返回
            if nums[mid] == target:
                return mid
            
            # 2. 判断哪一侧是有序区间
            
            # 2.1. 左侧 [left, mid] 是有序的 (包括相等，处理未旋转的情况)
            if nums[left] <= nums[mid]:
                # 判断 target 是否在有序的左侧区间内
                if nums[left] <= target and target < nums[mid]:
                    # target 在左侧有序区间，缩小右边界
                    right = mid - 1
                else:
                    # target 不在左侧有序区间，说明在右侧无序区间，缩小左边界
                    left = mid + 1
            
            # 2.2. 右侧 [mid, right] 是有序的 (当左侧无序时，右侧必有序)
            else: 
                # 判断 target 是否在有序的右侧区间内
                if nums[mid] < target and target <= nums[right]:
                    # target 在右侧有序区间，缩小左边界
                    left = mid + 1
                else:
                    # target 不在右侧有序区间，说明在左侧无序区间，缩小右边界
                    right = mid - 1
                    
        # 搜索结束，未找到 target
        return -1
