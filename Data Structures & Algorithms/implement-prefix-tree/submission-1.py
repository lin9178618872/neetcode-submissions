class TrieNode:
    """
    模拟C++的TrieNode结构
    """
    def __init__(self):
        # 字符和孩子指针的映射，使用Python字典
        self.children = {}  # {char: TrieNode}
        # node节点中的字符是否是某个字符串的结尾
        self.isEnd = False

class PrefixTree:
    """
    前缀树 (Trie) 的 Python 实现
    """
    def __init__(self):
        # 创建根节点
        self.m_root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向前缀树中插入一个单词
        """
        cur_node = self.m_root
        # 根据word构建前缀树
        for char in word:
            # 建立新节点和字符之间的映射关系
            # 相当于 C++ 中的 if (cur_node->children.count(word[i]) == 0)
            if char not in cur_node.children:
                # 相当于 C++ 中的 cur_node->children[word[i]] = new TrieNode();
                cur_node.children[char] = TrieNode()
            # 移动到下一个节点
            cur_node = cur_node.children[char]
        
        # 标记当前节点为一个单词的结尾
        cur_node.isEnd = True

    def search(self, word: str) -> bool:
        """
        查找前缀树中是否存在一个完整的单词
        """
        cur_node = self.m_root
        # 搜索前缀树
        for char in word:
            # 相当于 C++ 中的 if (cur_node->children.count(word[i]) == 0)
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        
        # 检查当前节点是否是某个单词的结尾
        return cur_node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        查找前缀树中是否存在任何以给定前缀开始的单词
        """
        cur_node = self.m_root
        for char in prefix:
            # 相当于 C++ 中的 if (cur_node->children.count(prefix[i]) == 0)
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
            
        return True

# 示例用法:
# obj = Trie()
# obj.insert("apple")
# param_2 = obj.search("apple") # True
# param_3 = obj.startsWith("app") # True
# print(f"Search 'apple': {param_2}")
# print(f"StartsWith 'app': {param_3}")