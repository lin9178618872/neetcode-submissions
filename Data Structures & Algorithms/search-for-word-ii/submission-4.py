from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        rows, cols = len(board), len(board[0])
        result = []

        def backtrack(r: int, c: int, node: TrieNode):
            ch = board[r][c]
            if ch not in node.children:
                return

            next_node = node.children[ch]

            if next_node.word != "":
                result.append(next_node.word)
                next_node.word = ""

            board[r][c] = "#"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    backtrack(nr, nc, next_node)

            board[r][c] = ch

            if not next_node.children:
                del node.children[ch]

        for i in range(rows):
            for j in range(cols):
                backtrack(i, j, root)

        return result

