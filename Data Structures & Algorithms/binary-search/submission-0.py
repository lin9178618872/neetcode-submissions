class Solution:
    # 标准的二分搜索框架，搜索目标元素的索引，若不存在则返回 -1
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1   # 注意：右边界是 len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1   # 注意：搜索右半区
            else:
                right = mid - 1  # 注意：搜索左半区
        
        return -1
