from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        
        if s_len != t_len:
            return False
        
        u_mapS = defaultdict(int)
        u_mapT = defaultdict(int)

        for i in range(len(s)):
            u_mapS[s[i]] += 1
            u_mapT[t[i]] += 1
        
        return u_mapS==u_mapT