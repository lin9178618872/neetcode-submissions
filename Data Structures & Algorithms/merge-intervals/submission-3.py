from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1) 先按起点排序
        intervals.sort(key=lambda x: x[0])

        # 2) output 用来存合并后的区间
        output = [intervals[0]]

        # 3) 从第二个区间开始遍历
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]   # output里最后一个区间的结尾

            # 4) 如果重叠：start <= lastEnd，合并
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                # 5) 不重叠：直接加入
                output.append([start, end])

        return output
