# Definition for an Interval.
# class Interval:
#     def __init__(self, start: int = None, end: int = None):
#         self.start = start
#         self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []

        # 1. 把所有员工的工作区间放到一个数组里
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)

        # 2. 按开始时间排序
        intervals.sort(key=lambda x: x.start)

        res = []

        # 3. 当前已经合并到的忙碌区间右端点
        prev_end = intervals[0].end

        # 4. 遍历后面的区间
        for interval in intervals[1:]:
            if interval.start > prev_end:
                # 说明中间有空闲时间
                res.append(Interval(prev_end, interval.start))

            # 更新当前忙碌时间的最远右端点
            prev_end = max(prev_end, interval.end)

        return res