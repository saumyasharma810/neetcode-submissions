class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        def it_exist(i,j,l):
            if l == len(word):
                print(i,j,l)
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != word[l]:
                return False
            if (i,j) in visited:
                return False
            visited.add((i,j))
            possible = False
            coords = [[1,0],[-1,0],[0,1],[0,-1]]
            for coord in coords:
                possible = possible or it_exist(i+coord[0], j+coord[1], l+1)
            print(i,j,l,possible)
            visited.remove((i,j))
            return possible


        for i in range(len(board)):
            for j in range(len(board[0])):
                if it_exist(i,j,0):
                    print(i,j)
                    return True
        
        return False


        