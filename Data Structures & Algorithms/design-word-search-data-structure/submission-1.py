class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not char in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.end = True

        

    def search(self, word: str) -> bool:
        def search_char(curr, ind):
            if ind == len(word):
                if curr.end:
                    return True
                return False
            if word[ind] == '.':
                there_is = False
                for childs in curr.children.keys():
                    there_is = there_is or search_char(curr.children[childs], ind+1)
                return there_is
            if word[ind] in curr.children:
                return search_char(curr.children[word[ind]], ind+1)
            return False
        return search_char(self.root, 0)
        

        
