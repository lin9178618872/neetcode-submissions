class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()
        
        for i, num in enumerate(nums):
            # 如果已经出现过 → 找到答案
            if num in seen:
                return True
            
            seen.add(num)
            
            # 保证窗口大小 <= k
            if len(seen) > k:
                seen.remove(nums[i - k])
        
        return False