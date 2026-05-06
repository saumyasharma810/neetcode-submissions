class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        can_flow_pacific = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        visited = set()
        for i in range(rows):
            can_flow_pacific[i][0] = 1
            queue.append((i,0))
        for i in range(cols):
            can_flow_pacific[0][i] = 1
            queue.append((0,i))
        # print(can_flow_pacific)
        pairs = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            r,c = queue[0][0], queue[0][1]
            queue.popleft()
            visited.add((r,c))
            can_flow_pacific[r][c] = 1
            for p in pairs:
                r_new, c_new = r+p[0], c+p[1]
                if 0 < r_new < rows and 0 < c_new < cols and heights[r_new][c_new] >= heights[r][c]:
                    if (r_new,c_new) not in visited:
                        visited.add((r_new,c_new))
                        queue.append((r_new,c_new))
                
        # print(can_flow_pacific)
        
        # print("done")
        can_flow_atlantic = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        visited = set()
        for i in range(rows):
            can_flow_atlantic[i][cols-1] = 1
            queue.append((i,cols-1))
        for i in range(cols):
            can_flow_atlantic[rows-1][i] = 1
            queue.append((rows-1,i))
        # print(can_flow_atlantic)
        while queue:
            r,c = queue[0][0], queue[0][1]
            queue.popleft()
            visited.add((r,c))
            can_flow_atlantic[r][c] = 1
            for p in pairs:
                r_new, c_new = r+p[0], c+p[1]
                if 0 <= r_new < rows and 0 <= c_new < cols and heights[r_new][c_new] >= heights[r][c]:
                    if (r_new,c_new) not in visited:
                        visited.add((r_new,c_new))
                        queue.append((r_new,c_new))
        # print(can_flow_atlantic)
        lst = []
        for i in range(rows):
            for j in range(cols):
                if can_flow_pacific[i][j] == 1 and  can_flow_atlantic[i][j] == 1:
                    lst.append([i,j])

        return lst

        
                        

          
        