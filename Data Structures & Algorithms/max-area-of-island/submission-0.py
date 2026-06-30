class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]

        print(len(visited))

        coords = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(i,j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0 or visited[i][j]:
                return 0
            visited[i][j] = True
            length = 0
            
            for coord in coords:
                length += dfs(i+coord[0], j+coord[1])
            
            return length+1

        max_len = 0

        for i in range(n):
            for j in range(m):
                max_len = max(max_len, dfs(i,j))
        
        return max_len

            

        