from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        u_mapRes = defaultdict(list) 
        
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            u_mapRes[tuple(count)].append(s)
            
        return list(u_mapRes.values())
