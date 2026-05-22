from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # 情况1：newInterval 在当前区间左边，且完全不重叠
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # 情况2：newInterval 在当前区间右边，且完全不重叠
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # 情况3：有重叠 -> 合并成更大的 newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # 如果循环结束还没 return，说明 newInterval 在最右边
        res.append(newInterval)
        return res
