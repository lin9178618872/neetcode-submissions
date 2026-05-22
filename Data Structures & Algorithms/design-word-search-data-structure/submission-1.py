class TrieNode:
    """
    字典树的节点结构
    """
    def __init__(self):
        # 字符和指向孩子节点的映射关系
        # 在 Python 中，使用字典 (dict) 代替 C++ 的 unordered_map<char, TrieNode*>
        self.children = {}
        # node节点是否是单词的结尾
        self.isWord = False

class WordDictionary:
    """
    实现一个支持 '.' 通配符的字典树
    """
    def __init__(self):
        # 字典树的根节点
        self.m_root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        将一个单词添加到字典树中
        """
        cur_node = self.m_root
        for char in word:
            # 如果当前字符的孩子节点不存在，则创建新的 TrieNode
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            # 移动到下一个节点
            cur_node = cur_node.children[char]
        
        # 标记当前节点是单词的结尾
        cur_node.isWord = True

    def search(self, word: str) -> bool:
        """
        搜索字典树中是否存在该单词，支持 '.' 作为通配符
        """
        return self._search_help(word, self.m_root, 0)

    def _search_help(self, word: str, root_node: TrieNode, index: int) -> bool:
        """
        递归辅助函数进行搜索
        """
        cur_node = root_node
        
        for i in range(index, len(word)):
            char = word[i]
            
            if char == '.':
                # 遇到通配符 '.'
                # 递归搜索当前节点的所有非空孩子节点
                for child_node in cur_node.children.values():
                    # 只要有一条路径（任何一个孩子节点）能够完成匹配，就返回 True
                    if self._search_help(word, child_node, i + 1):
                        return True
                
                # 如果所有路径都不能匹配，则返回 False
                return False
            else:
                # 遇到普通字符
                if char not in cur_node.children:
                    # 如果当前字符没有对应的孩子节点，则匹配失败
                    return False
                
                # 移动到下一个节点
                cur_node = cur_node.children[char]
        
        # 遍历完整个 word 后，检查当前节点是否是一个完整的单词的结尾
        return cur_node.isWord

# 示例使用方法：
# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad"))  # False
# print(obj.search("bad"))  # True
# print(obj.search(".ad"))  # True
# print(obj.search("b.."))  # True
# print(obj.search("b."))   # False