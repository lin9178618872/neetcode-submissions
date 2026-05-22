class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        u_mapS = {}
        u_mapT = {}

        for i in range(len(s)):
            u_mapS[s[i]] = u_mapS.get(s[i], 0) + 1
            u_mapT[t[i]] = u_mapT.get(t[i], 0) + 1
        
        return u_mapS == u_mapT
