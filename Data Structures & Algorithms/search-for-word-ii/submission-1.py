class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        n,m = len(board), len(board[0])

        def add_in_trie(ind):
            curr = root
            for char in words[ind]:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.index = ind


        for i in range(len(words)):
            add_in_trie(i)

        x_axis = [1,0,-1,0]
        y_axis = [0,1,0,-1]

        lst = []

        def dfs(i,j,visited,curr):
            # print("a",i,j)
            if board[i][j] not in curr.children:
                return
            if (i,j) in visited:
                return
            curr = curr.children[board[i][j]]
            # print("b",i,j)
            if curr.index != -1:
                lst.append(words[curr.index])
                curr.index = -1
            visited.add((i,j))
            for k in range(4):
                if i+x_axis[k] >= n or i+x_axis[k] < 0:
                    continue
                if j+y_axis[k] >= m or j+y_axis[k] < 0:
                    continue
                dfs(i+x_axis[k],j+y_axis[k],visited, curr)
            # print("c",i,j)
            # print(visited)
            visited.remove((i,j))

        visited = set()
        for i in range(n):
            for j in range(m):
                dfs(i,j,visited,root) 

        return lst
            


        

        
        