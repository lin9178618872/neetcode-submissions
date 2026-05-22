class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals_len = len(intervals)
        if intervals_len == 0:
            return 0

        intervals.sort(key=lambda x: x[0])
        res = 0
        tmpEnd = intervals[0][1]

        for i in range(1, intervals_len):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            if current_start >= tmpEnd:
                tmpEnd = current_end
            else:
                res += 1
                tmpEnd = min(tmpEnd, current_end)

        return res
