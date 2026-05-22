# Definition for an Interval.
# class Interval:
#     def __init__(self, start: int = None, end: int = None):
#         self.start = start
#         self.end = end
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []

        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        free = []

        for i in range(1, len(merged)):
            prev_end = merged[i - 1][1]
            curr_start = merged[i][0]

            if prev_end < curr_start:
                free.append(Interval(prev_end, curr_start))

        return free