class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board), len(board[0])

        queue = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == n-1 or j == m-1) and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
        coords = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for cord in coords:
                    i,j = node[0]+cord[0], node[1]+cord[1]
                    if i >= 0 and j >= 0 and i < n and j < m and (i,j) not in visited and board[i][j] == 'O':
                        queue.append((i,j))
                        visited.add((i,j))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
            
        

                    

                    

        

        