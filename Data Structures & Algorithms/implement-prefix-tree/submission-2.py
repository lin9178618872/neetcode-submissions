class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class PrefixTree:
    def __init__(self):
        self.m_root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.m_root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.isEnd = True

    def search(self, word: str) -> bool:
        cur_node = self.m_root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return cur_node.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.m_root
        for char in prefix:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return True
