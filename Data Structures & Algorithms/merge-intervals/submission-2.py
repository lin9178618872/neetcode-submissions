class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        res = []
        tempStart = intervals[0][0]
        tempEnd = intervals[0][1]

        for i in range(len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            if current_start <= tempEnd:
                tempEnd = max(tempEnd, current_end)
            else:
                res.append([tempStart, tempEnd])
                tempStart = current_start
                tempEnd = current_end

        res.append([tempStart, tempEnd])
        return res
