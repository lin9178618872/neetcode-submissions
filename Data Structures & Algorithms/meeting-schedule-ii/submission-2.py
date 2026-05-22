"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for interval in intervals:
            # meeting starts -> need one more room
            events.append((interval.start, 1))

            # meeting ends -> free one room
            events.append((interval.end, -1))

        # 同一时间先处理 end(-1)，再处理 start(1)
        events.sort()

        rooms = 0
        ans = 0

        for _, change in events:
            rooms += change
            ans = max(ans, rooms)

        return ans