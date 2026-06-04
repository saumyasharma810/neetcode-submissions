class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1]*n for _ in range(m)]

        def paths(i,j):
            if i == m:
                return 1
            if j == n:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = paths(i+1,j) + paths(i,j+1)
            return dp[i][j]
        
        return paths(1,1)
            
        