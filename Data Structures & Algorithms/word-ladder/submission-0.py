class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited = set()
        queue = deque()
        queue.append(beginWord)
        visited.add(beginWord)

        def diff(a,b):
            n = len(a)
            cnt = 0
            for i in range(n):
                if a[i]!=b[i]:
                    cnt+=1
            return True if cnt <= 1 else False

        l = 1
        while queue:
            l+=1
            # print(l)
            # print(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                for word in wordList:
                    if word not in visited and diff(node,word):
                        if word == endWord:
                            return l
                        # print(word)
                        queue.append(word)
                        visited.add(word)
        return 0
                    

        