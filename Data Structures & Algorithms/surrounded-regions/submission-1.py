class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board), len(board[0])

        def dfs1(i,j,visited):
            if i == 0 or j == 0 or i == n-1 or j == m-1:
                return True
            coords = [[1,0],[-1,0],[0,1],[0,-1]]
            visited.add((i,j))
            found = False
            for c in coords:
                if i+c[0] >= 0 and j+c[1] >= 0 and i+c[0] < n and j+c[1] < m and board[i+c[0]][j+c[1]]=='O' and (i+c[0], j+c[1]) not in visited:
                    found = found or dfs1(i+c[0], j+c[1],visited)
            visited.remove((i,j))
            return found
        
        def dfs2(i,j,visited,change):
            coords = [[1,0],[-1,0],[0,1],[0,-1]]
            visited.add((i,j))
            if change:
                board[i][j] = 'X'
            for c in coords:
                if i+c[0] >= 0 and j+c[1] >= 0 and i+c[0] < n and j+c[1] < m and board[i+c[0]][j+c[1]]=='O' and (i+c[0], j+c[1]) not in visited:
                    dfs2(i+c[0], j+c[1],visited,change)


        visited = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i,j) not in visited:
                    if not dfs1(i,j,visited):
                        dfs2(i,j,visited,True)
                    else:
                        dfs2(i,j,visited,False)

                    

        

        