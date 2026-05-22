class Solution:
    """
    合并区间 (Merge Intervals) 问题。
    首先按区间起始点排序，然后进行一次遍历合并重叠区间。
    """
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        # 边界条件：如果数组为空，直接返回空列表
        if not intervals:
            return []
        
        # 1. 排序
        # C++ 使用自定义的 lambda 表达式按第一个元素 (intervals[i][0]) 排序。
        # Python 使用 list.sort() 或 sorted()，默认按列表的第一个元素排序。
        intervals.sort(key=lambda x: x[0])
        
        # 2. 初始化结果列表和当前正在合并的区间
        res = []
        
        # tempStart 和 tempEnd 存储当前正在合并的区间的起始和结束
        # 初始值设为第一个区间
        tempStart = intervals[0][0]
        tempEnd = intervals[0][1]
        
        # 3. 遍历并合并
        # 遍历所有区间 (包括第一个，因为第一个区间被用于初始化 tempStart/tempEnd)
        for i in range(len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            
            # 检查：当前区间是否与正在合并的区间重叠或相邻
            # 重叠条件：当前区间的起始点 <= 正在合并的区间的结束点
            if current_start <= tempEnd:
                
                # 如果重叠，更新合并区间的结束点，取两者中的最大值
                tempEnd = max(tempEnd, current_end)
                
            # 检查：两个区间没有重叠
            else:
                # 3a. 将前面已经合并好的区间添加到结果中
                res.append([tempStart, tempEnd])
                
                # 3b. 将当前区间 (intervals[i]) 作为新的合并区间的起点
                tempStart = current_start
                tempEnd = current_end
                
        # 4. 边界情况：添加最后一个合并后的区间
        # 循环结束后，tempStart 和 tempEnd 仍然保存着最后一个合并好的区间，需要将其添加到 res 中。
        res.append([tempStart, tempEnd])
        
        return res

# 示例用法
# solution = Solution()
# print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))  # 输出: [[1, 6], [8, 10], [15, 18]]
# print(solution.merge([[1,4],[4,5]]))                # 输出: [[1, 5]]