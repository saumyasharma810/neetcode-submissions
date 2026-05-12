class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        i,j = 0,n-1
        while i<j:
            # each row
            for l in range(i,j):
                row,col = i,l
                temp = matrix[row][col]
                for _ in range(4):
                    new_row, new_col = col, n-1-row
                    temp2 = matrix[new_row][new_col]
                    matrix[new_row][new_col] = temp
                    temp = temp2
                    row,col = new_row, new_col
            i+=1
            j-=1


        
        