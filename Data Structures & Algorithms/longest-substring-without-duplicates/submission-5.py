class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left=0
        right=0
        res = 0

        while right < len(s):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            right += 1

            while window[c] > 1:
                d = s[left]
                window[d] -= 1
                left += 1

            res = max(res, right - left)

        return res
