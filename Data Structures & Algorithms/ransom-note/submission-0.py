class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_r = {}
        count_m = {}

        # 统计 ransomNote
        for c in ransomNote:
            if c in count_r:
                count_r[c] += 1
            else:
                count_r[c] = 1

        # 统计 magazine
        for c in magazine:
            if c in count_m:
                count_m[c] += 1
            else:
                count_m[c] = 1

        # 检查是否够用
        for c in count_r:
            if c not in count_m or count_m[c] < count_r[c]:
                return False

        return True