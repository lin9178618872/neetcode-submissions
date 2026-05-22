class Solution:
    """
    插入区间 (Insert Interval) 问题。
    将 newInterval 插入到已排序的 intervals 列表中，并合并重叠区间。
    """
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        res = []
        
        # 定义 newInterval 的起始和结束
        new_start, new_end = newInterval[0], newInterval[1]
        
        i = 0
        intervals_len = len(intervals)
        
        # --- 1. 处理不重叠在左边的区间 ---
        # 将所有在 newInterval 左侧且不重叠的区间添加到结果中
        # 条件: 当前区间的结束时间 < newInterval 的开始时间
        while i < intervals_len and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1
            
        # --- 2. 处理重叠的区间并合并 ---
        # 此时 intervals[i] 是第一个与 newInterval 可能重叠或紧邻的区间
        # 条件: 当前区间的开始时间 <= newInterval 的结束时间
        while i < intervals_len and intervals[i][0] <= new_end:
            # 合并操作：更新 newInterval 的开始时间和结束时间
            
            # 合并的开始时间取两者中的最小值
            new_start = min(new_start, intervals[i][0])
            
            # 合并的结束时间取两者中的最大值
            new_end = max(new_end, intervals[i][1])
            
            i += 1
            
        # --- 3. 添加合并后的 newInterval ---
        # 经过合并循环后，new_start 和 new_end 存储了最终合并后的区间
        res.append([new_start, new_end])
        
        # --- 4. 处理不重叠在右边的区间 ---
        # 将剩余所有区间（它们都在合并后的 newInterval 右侧且不重叠）添加到结果中
        while i < intervals_len:
            res.append(intervals[i])
            i += 1
            
        return res
        
    # --- 另一种直接翻译 C++ 逻辑的方法 (更接近原代码结构) ---
    def insert_direct_translation(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        intervals_len = len(intervals)
        
        for i in range(intervals_len):
            # 情况 1: newInterval 在 intervals[i] 的左边且不重叠
            # 即新区间完全位于当前区间之前
            if newInterval[1] < intervals[i][0]:
                # 1a. 添加 newInterval
                res.append(newInterval)
                # 1b. 将剩余的区间全部加入 res
                for j in range(i, intervals_len):
                    res.append(intervals[j])
                # 1c. 结束并返回
                return res
            
            # 情况 2: newInterval 在 intervals[i] 的右边且不重叠
            # 即新区间完全位于当前区间之后
            elif newInterval[0] > intervals[i][1]:
                # 仅将 intervals[i] 加入 res
                res.append(intervals[i])
            
            # 情况 3: newInterval 和 intervals[i] 重叠
            else:
                # 更新 newInterval 为合并后的区间
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                
        # 循环结束：如果 newInterval 还没有被添加到 res 中（即没有触发 '情况 1'）
        # 说明 newInterval 是最后一个区间，或者与前面的区间合并后成为最后一个区间。
        res.append(newInterval)
        return res