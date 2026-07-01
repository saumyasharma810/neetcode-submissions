class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        coords = [[1,0],[-1,0],[0,1],[0,-1]]

        ans = 0

        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for coord in coords:
                    new_i, new_j = i+coord[0], j+coord[1]
                    if new_i >=0 and new_j >=0 and new_i < n and new_j < m and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        queue.append((new_i,new_j))
            if queue:
                ans+=1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return ans


        