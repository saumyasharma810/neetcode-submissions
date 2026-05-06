class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        visited = set()
        x_axis, y_axis = [0,1,0,-1], [1,0,-1,0]

        def dfs(i,j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if grid[i][j] == '0':
                return
            if (i,j) in visited:
                return
            visited.add((i,j))
            for k in range(4):
                dfs(i+x_axis[k],j+y_axis[k])
                    


        count = 0
        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] == '1':
                    dfs(i,j)
                    count+=1
        
        return count


        