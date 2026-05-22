class TrieNode:
    """
    Trie (前缀树) 的节点。
    """
    def __init__(self):
        # 字符和指向孩子节点指针的映射关系
        # 使用字典代替 C++ 的 unordered_map<char, TrieNode*>
        self.children = {}
        # 既可以用来判断当前节点是否为单词的结尾，又可以保存单词
        # 使用空字符串 "" 代替 C++ 中的默认构造函数的初始化
        self.word = ""

    def insert(self, word: str):
        """
        向前缀树中插入一个单词。
        """
        cur_node = self
        for char in word:
            if char not in cur_node.children:
                # 建立新节点和字符之间的映射关系
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        
        # 标记当前节点为一个单词的结尾并存储单词
        cur_node.word = word

class Solution:
    """
    查找单词的解决方案类。
    """
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        在给定字母矩阵中查找给定单词列表中的单词。
        """
        root = TrieNode()
        # 根据给定的单词构造前缀树
        for word in words:
            root.insert(word)

        # 使用 set 自动去重，存储找到的单词
        res_set = set()
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                # 矩阵的每一个元素做为起点开始搜索
                self._findWords_help(board, r, c, root, res_set)
        
        # 将 set 转换为 list 返回
        return list(res_set)

    def _findWords_help(self, board: list[list[str]], row: int, col: int, node: TrieNode, res_set: set):
        """
        深度优先搜索 (DFS) 辅助函数。
        """
        rows, cols = len(board), len(board[0])
        
        # 1. 越界检查
        if not (0 <= row < rows and 0 <= col < cols):
            return
        
        char = board[row][col]
        # 2. 访问检查 (使用 '#' 代替 C++ 中的 '*' 标记已访问)
        if char == '#': 
            return
        
        # 3. 前缀树检查：当前字符是否在前缀树的子节点中
        if char not in node.children:
            return

        # 移动到下一个节点
        node = node.children[char]
        
        # 检查是否找到一个完整的单词
        if node.word != "":
            # 将找到的单词添加到结果集中 (set 会自动去重)
            # 这里不能 return，因为当前找到的单词有可能是另一个更长单词的前缀
            res_set.add(node.word)
            
            # 【优化】找到一个单词后，可以将其从前缀树中移除，以避免重复搜索。
            # 这需要额外的逻辑来处理节点的删除，为了保持代码的直接转换，暂时省略。

        # 标记当前字符为已访问
        board[row][col] = '#'
        
        # 搜索前后左右相邻的字符
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 右、左、下、上
        for dr, dc in directions:
            self._findWords_help(board, row + dr, col + dc, node, res_set)
        
        # 回溯：将字符恢复到矩阵中，以便其他路径可以访问
        board[row][col] = char


# 示例使用 (假设用户想看到如何使用)
"""
if __name__ == '__main__':
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words = ["oath","pea","eat","rain", "hklr", "oaa"]
    
    solution = Solution()
    result = solution.findWords(board, words)
    print(f"找到的单词: {result}") # 预期输出示例: ['oath', 'eat', 'oaa', 'hklr'] (顺序可能不同)
"""