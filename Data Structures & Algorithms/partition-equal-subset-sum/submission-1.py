class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = set()
        dp.add(0)

        for num in nums:
            new_dp = set()

            for s in dp:
                if s + num == target:
                    return True
                new_dp.add(s + num)
                new_dp.add(s)

            dp = new_dp

        return False