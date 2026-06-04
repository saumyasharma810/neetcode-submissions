class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if j >0:
                    dp[i][j-1] += dp[i][j]
                if i > 0:
                    dp[i-1][j] += dp[i][j]



        return dp[0][0]


        # def paths(i,j):
        #     if i == m:
        #         return 1
        #     if j == n:
        #         return 1
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     dp[i][j] = paths(i+1,j) + paths(i,j+1)
        #     return dp[i][j]
        
        # return paths(1,1)
            
        