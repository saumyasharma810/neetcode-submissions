class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i,j = 0,0
        change_col = True
        change_row = False
        inc_row = True 
        inc_col = True
        order = []
        n,m = len(matrix), len(matrix[0])
        min_col, min_row, max_col, max_row = 0,1,m-1,n-1
        while len(order)!=n*m:
            order.append(matrix[i][j])
            if change_col:
                if inc_col:
                    j+=1
                    if j == max_col+1:
                        j-=1
                        i+=1
                        inc_col = False
                        change_col = False
                        change_row = True
                        max_col-=1
                        
                else:
                    j-=1
                    if j == min_col-1:
                        j+=1
                        i-=1
                        inc_col = True
                        change_col = False
                        change_row = True
                        min_col+=1
                

            elif change_row:
                if inc_row:
                    i+=1
                    if i == max_row+1:
                        i-=1
                        j-=1
                        inc_row = False
                        change_row = False
                        change_col = True
                        max_row-=1
                else:
                    i-=1
                    if i == min_row-1:
                        i+=1
                        j+=1
                        inc_row = True
                        change_row = False
                        change_col = True
                        min_row+=1

            else:
                print("hello")
                break
        return order
            
            
            

        
        