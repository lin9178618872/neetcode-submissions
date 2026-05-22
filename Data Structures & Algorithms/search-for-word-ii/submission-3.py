class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

    def insert(self, word: str):
        cur_node = self
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.word = word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for word in words:
            root.insert(word)

        res_set = set()
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                self._findWords_help(board, r, c, root, res_set)

        return list(res_set)

    def _findWords_help(
        self,
        board: list[list[str]],
        row: int,
        col: int,
        node: TrieNode,
        res_set: set
    ):
        rows, cols = len(board), len(board[0])

        if not (0 <= row < rows and 0 <= col < cols):
            return

        char = board[row][col]
        if char == '#':
            return

        if char not in node.children:
            return

        node = node.children[char]

        if node.word != "":
            res_set.add(node.word)

        board[row][col] = '#'

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            self._findWords_help(board, row + dr, col + dc, node, res_set)

        board[row][col] = char
