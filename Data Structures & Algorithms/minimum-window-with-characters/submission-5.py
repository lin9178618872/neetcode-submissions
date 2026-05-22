class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 用普通字典代替 Counter
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        required_count = len(need)
        valid = 0
        
        left, right = 0, 0
        min_len = float('inf')
        start_index = -1

        while right < len(s):
            c = s[right]
            right += 1
            
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == required_count:
                current_len = right - left
                if current_len < min_len:
                    min_len = current_len
                    start_index = left
                    
                d = s[left]
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1

        if start_index == -1:
            return ""
        else:
            return s[start_index:start_index + min_len]

