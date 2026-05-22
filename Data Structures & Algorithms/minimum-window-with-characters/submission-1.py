from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. target_needs: 存储 t 中字符及其所需数量（即目标需求）
        target_needs = Counter(t)
        
        # 2. window_counts: 存储当前窗口 [left, right) 中字符的出现次数
        window_counts = {}
        
        # required_count: t 中不同字符的种类数量
        required_count = len(target_needs)
        
        # valid: 窗口中满足 target_needs 要求的不同字符的数量
        valid = 0
        
        left, right = 0, 0
        
        # 初始化结果记录
        min_len = float('inf')  # 记录最短窗口长度
        start_index = -1        # 记录最短窗口的起始位置

        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            
            # 增大窗口
            right += 1
            
            # 进行窗口内数据的一系列更新 (1/2): 
            # 增加 c 的计数，并判断是否满足了 c 的需求
            if c in target_needs:
                # 更新 window_counts
                window_counts[c] = window_counts.get(c, 0) + 1
                
                # 如果 c 的数量首次达到 target_needs[c]，则 valid + 1
                if window_counts[c] == target_needs[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩 (window needs shrink)
            # 满足条件：窗口中所有 t 中的字符都已包含（包括数量）
            while valid == required_count:
                # 更新答案：当前窗口 [left, right) 是一个可行解
                current_len = right - left
                if current_len < min_len:
                    min_len = current_len
                    start_index = left
                    
                # d 是将移出窗口的字符
                d = s[left]
                
                # 进行窗口内数据的一系列更新 (2/2): 
                # 减少 d 的计数，并判断是否破坏了 d 的需求
                if d in target_needs:
                    # 如果 d 的数量在减少前等于 target_needs[d]，
                    # 说明移出 d 后，该字符的需求不再满足，valid 减 1
                    if window_counts[d] == target_needs[d]:
                        valid -= 1
                    
                    # 更新 window_counts
                    window_counts[d] -= 1
                    
                # 缩小窗口
                left += 1

        # 根据记录的最短长度和起始位置返回结果
        if start_index == -1:
            return ""
        else:
            return s[start_index : start_index + min_len]