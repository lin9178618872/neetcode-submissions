class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(k):

            total_time = 0

            for pile in piles:

                if pile % k == 0:
                    hours = pile // k
                else:
                    hours = pile // k + 1

                total_time = total_time + hours

            if total_time <= h:
                return True
            else:
                return False


        left = 1
        right = max(piles)

        while left <= right:

            mid = (left + right) // 2

            if can_finish(mid) == True:
                right = mid - 1
            else:
                left = mid + 1

        return left

