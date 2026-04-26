class PrefixTree:
    original_trie = []

    def __init__(self):
        self.original_trie = [[]] * 26

    def insert(self, word: str) -> None:
        trie = self.original_trie
        for char in word:
            # print(char)
            # print(trie[ord(char)-ord('a')])
            if not trie[ord(char)-ord('a')]:
                # print("hell0")
                trie[ord(char)-ord('a')] = [False,[()]*26]
            
            if char == word[len(word)-1]:
                trie[ord(char)-ord('a')][0] = True
            # print(trie[ord(char)-ord('a')][0])
            trie = trie[ord(char)-ord('a')][1]



    def search(self, word: str) -> bool:
        trie = self.original_trie
        found = False
        for char in word:
            if not trie[ord(char)-ord('a')]:
                return False
            found = trie[ord(char)-ord('a')][0]
            trie = trie[ord(char)-ord('a')][1]
        return found


    def startsWith(self, prefix: str) -> bool:
        trie = self.original_trie
        for char in prefix:
            if not trie[ord(char)-ord('a')]:
                return False
            trie = trie[ord(char)-ord('a')][1]
        return True
        
        