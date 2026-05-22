class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.m_root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.m_root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.isWord = True

    def search(self, word: str) -> bool:
        return self._search_help(word, self.m_root, 0)

    def _search_help(self, word: str, root_node: TrieNode, index: int) -> bool:
        cur_node = root_node
        for i in range(index, len(word)):
            char = word[i]
            if char == '.':
                for child_node in cur_node.children.values():
                    if self._search_help(word, child_node, i + 1):
                        return True
                return False
            else:
                if char not in cur_node.children:
                    return False
                cur_node = cur_node.children[char]
        return cur_node.isWord
