class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m = len(matrix), len(matrix[0])
        # row_list = [False] * n
        # col_list = [False] * m
        row_1 = False
        col_1 = False
        for j in range(m):
            if matrix[0][j] == 0:
                row_1 = True
        for i in range(n):
            if matrix[i][0] == 0:
                col_1 = True
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1,n):
            for j in range(1,m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if row_1:
            for j in range(m):
                matrix[0][j] = 0
        if col_1:
            for i in range(n):
                matrix[i][0] = 0
            



        
        