class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            ind = ord(char)-ord('a')
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.end = True



    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            ind = ord(char)-ord('a')
            if not curr.children[ind]:
                return False
            curr = curr.children[ind]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            ind = ord(char)-ord('a')
            if not curr.children[ind]:
                return False
            curr = curr.children[ind]
        return True
        