class Solution:
    """
    无重叠区间 (Non-overlapping Intervals) 问题，使用贪心算法实现。
    
    目标: 移除最少数量的区间，使得剩下的区间互不重叠。
    策略: 遍历排序后的区间，遇到重叠时，保留结束点更小的那个区间，并移除结束点较大的那个区间。
    """
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals_len = len(intervals)
        if intervals_len == 0:
            return 0
        
        # 1. 排序
        # C++ 代码按起始点 (intervals[i][0]) 排序。
        # Python 使用 list.sort() 并指定按第一个元素排序。
        intervals.sort(key=lambda x: x[0])
        
        # 2. 初始化
        # res 存储需要移除的区间数量
        res = 0
        
        # tmpEnd 存储当前已选择的、最后一个不重叠区间的结束点
        # 初始化为第一个区间的结束点
        tmpEnd = intervals[0][1]
        
        # 3. 遍历并判断是否重叠
        # 从第二个区间开始遍历 (索引 i = 1)
        for i in range(1, intervals_len):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            
            # --- 情况 1: 没有重叠 ---
            # 当前区间的起始点 >= 已选择的最后一个区间的结束点
            if current_start >= tmpEnd:
                # 保留当前区间，更新 tmpEnd 为当前区间的结束点
                tmpEnd = current_end
                
            # --- 情况 2: 有重叠 ---
            # 当前区间的起始点 < 已选择的最后一个区间的结束点
            else:
                # 移除重叠区间，res 计数器加 1
                res += 1
                
                # 贪心选择: 保留结束点较小的那个区间
                # 即：如果 tmpEnd 和 current_end 发生重叠，
                # 我们选择留下结束点较小的那个，因为结束点小的更有利于后续区间的接入。
                # 这里的 tmpEnd 是上一个已选择的区间的结束点，
                # current_end 是当前区间的结束点。
                tmpEnd = min(tmpEnd, current_end)
                
        return res

# 示例用法
# solution = Solution()
# print(solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # 输出: 1 (移除 [1,3])
# print(solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))      # 输出: 2 (移除两个 [1,2])
# print(solution.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])) # 输出: 3