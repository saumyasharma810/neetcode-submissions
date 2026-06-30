class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid), len(grid[0])
        queue = deque()
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    # print("hello",i,j)
                    queue.append((i,j))
                    visited[i][j] = True


        coords = [[1,0],[-1,0],[0,1],[0,-1]]

        dist = 1
        while queue:
            print(dist)
            for _ in range(len(queue)):
                # print(queue[0])
                i,j = queue.popleft()
                # print(i,j)
                for coord in coords:
                    new_i = i+coord[0]
                    new_j = j+coord[1]
                    if new_i >= 0 and new_j >=0 and new_i < n and new_j < m and (not visited[new_i][new_j]) and grid[new_i][new_j] != -1:
                        queue.append((new_i, new_j))
                        visited[new_i][new_j] = True
                        grid[new_i][new_j] = dist
            dist+=1
        
        

                    
                
