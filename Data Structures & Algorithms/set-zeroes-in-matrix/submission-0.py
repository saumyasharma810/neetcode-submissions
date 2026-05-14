class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m = len(matrix), len(matrix[0])
        row_list = [False] * n
        col_list = [False] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_list[i] = True
                    col_list[j] = True
        for i in range(n):
            for j in range(m):
                if row_list[i] or col_list[j]:
                    matrix[i][j] = 0


        
        