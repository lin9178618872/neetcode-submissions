from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        u_mapRes = {}   # 普通字典
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            
            # 手动判断 key 是否存在
            if key not in u_mapRes:
                u_mapRes[key] = []
            
            u_mapRes[key].append(s)
            
        return list(u_mapRes.values())
