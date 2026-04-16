class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, b = 0, len(matrix)-1
        while u<b:
            print(u,b)
            mid = (u+b)//2
            if matrix[mid][0] > target:
                b = mid-1
            elif matrix[mid][0] <= target and matrix[mid+1][0] > target:
                u = mid
                break
            else:
                u = mid + 1
        print(u)
        row = matrix[u]
        l,r = 0,len(row)-1
        print(row)
        while l<r:
            print(l,r)
            mid = (l+r)//2
            if row[mid] > target:
                r = mid-1
            elif row[mid] < target:
                l = mid+1
            else:
                return True
        return row[l]==target
