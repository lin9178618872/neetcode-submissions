from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([beginWord])
        visited = set([beginWord])
        step = 1

        while q:
            sz = len(q)

            for _ in range(sz):
                cur = q.popleft()

                if cur == endWord:
                    return step

                for i in range(len(cur)):
                    cur_list = list(cur)
                    old_char = cur_list[i]

                    for c in range(26):
                        new_char = chr(ord('a') + c)

                        if new_char == old_char:
                            continue

                        cur_list[i] = new_char
                        nxt = "".join(cur_list)

                        if nxt in wordSet and nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)

            step += 1

        return 0