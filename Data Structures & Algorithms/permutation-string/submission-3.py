class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # 1. 普通字典
        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        left = 0
        right = 0
        valid = 0

        while right < len(s2):
            c = s2[right]
            right += 1

            # 更新窗口
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 收缩窗口
            while right - left >= len(s1):
                if valid == len(need):
                    return True

                d = s2[left]
                left += 1

                if d in need:
                    if window.get(d, 0) == need[d]:
                        valid -= 1
                    window[d] = window.get(d, 0) - 1

        return False

