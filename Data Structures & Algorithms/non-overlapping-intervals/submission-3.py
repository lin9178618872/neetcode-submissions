from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1) 先按照区间的起点排序（默认先比 start，再比 end）
        intervals.sort()

        # 2) res 用来统计：需要删除多少个区间
        res = 0

        # 3) prevEnd 表示：当前保留下来的区间的“结束位置”
        #    一开始先把第一个区间留下，所以 prevEnd = 第一个区间的 end
        prevEnd = intervals[0][1]

        # 4) 从第二个区间开始，一个一个检查
        for start, end in intervals[1:]:
            
            # ✅ 情况1：不重叠
            # start >= prevEnd 说明新区间从 prevEnd 之后开始，不会撞到之前的区间
            if start >= prevEnd:
                # 那我们就把新区间留下，并更新 prevEnd
                prevEnd = end
            
            # ❌ 情况2：重叠
            else:
                # 发生重叠：必须删掉一个区间，所以 res + 1
                res += 1

                # 关键贪心：
                # 重叠时我们应该留下“结束更早”的区间
                # 因为结束越早，后面越容易接更多区间
                prevEnd = min(prevEnd, end)

        # 5) 返回需要删除的区间数量
        return res
