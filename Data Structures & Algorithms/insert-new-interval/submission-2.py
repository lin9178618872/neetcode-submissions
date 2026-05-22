class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        new_start, new_end = newInterval[0], newInterval[1]
        i = 0
        intervals_len = len(intervals)

        while i < intervals_len and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1

        while i < intervals_len and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        res.append([new_start, new_end])

        while i < intervals_len:
            res.append(intervals[i])
            i += 1

        return res

    def insert_direct_translation(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        intervals_len = len(intervals)

        for i in range(intervals_len):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                for j in range(i, intervals_len):
                    res.append(intervals[j])
                return res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)
        return res
