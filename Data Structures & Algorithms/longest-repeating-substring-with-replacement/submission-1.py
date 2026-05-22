class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1. window: 记录窗口中每个字符的出现次数
        # 因为只有大写英文字符，可以使用一个长度为 26 的数组代替 Map
        char_counts = [0] * 26  
        
        left, right = 0, 0
        max_len = 0          # 最终返回的最长子串长度
        max_freq = 0         # 窗口内出现次数最多的字符的次数

        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            
            # 进行窗口内数据的一系列更新 (1/2): 增加新字符的计数
            # 字符 'A' 对应的索引是 0, 'B' 是 1, 以此类推
            char_counts[ord(c) - ord('A')] += 1
            
            # 更新 max_freq：当前窗口内出现次数最多的字符的次数
            # 注意： max_freq 只需要记录历史最大值，即使在收缩窗口时，
            # 它不严格要求是当前窗口的最大频率，但只要 max_len 不减小，就没问题。
            # 简单的做法是：max_freq = max(max_freq, char_counts[ord(c) - ord('A')])
            # 这种做法是有效的，因为它保证了我们只会尝试进一步延长当前找到的最长子串。
            max_freq = max(max_freq, char_counts[ord(c) - ord('A')])

            # 增大窗口
            right += 1
            
            # 判断左侧窗口是否要收缩 (window needs shrink)
            # 窗口长度 L = right - left
            # 需要替换的次数 = L - max_freq
            # 收缩条件： L - max_freq > k
            window_len = right - left
            while window_len - max_freq > k:
                # d 是将移出窗口的字符
                d = s[left]
                
                # 进行窗口内数据的一系列更新 (2/2): 减少移出字符的计数
                char_counts[ord(d) - ord('A')] -= 1
                
                # 缩小窗口
                left += 1
                
                # 更新当前窗口长度（供下次循环判断）
                window_len = right - left
                # 注意：这里不需要更新 max_freq，因为即使左侧字符 d 移出导致 max_freq 减小，
                # 我们也只关心当前最长的、满足条件的子串，
                # 不更新 max_freq 相当于我们只在窗口长度大于 max_len 时才有可能更新 max_len。
            
            # 更新答案：当前窗口 [left, right) 满足 window_len - max_freq <= k
            # 也就是说，这是一个有效的子串。
            # 由于 left 只有在不满足条件时才移动，当循环结束时，
            # 窗口 [left, right) 必然是满足条件的子串中最长的一个（对于当前的 right 而言）。
            max_len = max(max_len, right - left)

        return max_len