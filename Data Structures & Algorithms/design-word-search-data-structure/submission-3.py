class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def backtrack(i: int, node: TrieNode) -> bool:
            if i == len(word):
                return node.isEnd

            ch = word[i]

            if ch != '.':
                if ch not in node.children:
                    return False
                return backtrack(i + 1, node.children[ch])

            for next_ch in node.children:
                if backtrack(i + 1, node.children[next_ch]):
                    return True

            return False

        return backtrack(0, self.root)

