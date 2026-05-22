from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # 1. window / need
        need = defaultdict(int)
        window = defaultdict(int)

        for c in s1:
            need[c] += 1

        # 2. 滑动窗口边界
        left, right = 0, 0
        valid = 0  # 已满足 need 的字符种类数

        # 3. 右指针移动
        while right < len(s2):
            c = s2[right]
            right += 1

            # 更新窗口
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 4. 判断是否需要收缩（窗口大小 >= s1 长度）
            while right - left >= len(s1):
                # 如果窗口完全匹配
                if valid == len(need):
                    return True

                d = s2[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return False
