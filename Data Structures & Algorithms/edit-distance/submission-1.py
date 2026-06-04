class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[-1] * len(word2) for _ in range(len(word1))]
        # dp[0][1] = 1
        # print(dp)

        def ops(i,j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1 
            if dp[i][j] != -1:
                return dp[i][j]
            value = min(ops(i,j-1)+1, ops(i-1,j)+1, ops(i-1,j-1)+1)
            if i>=0 and j>=0 and word1[i] == word2[j]:
                value = min(value, ops(i-1,j-1))
            dp[i][j] = value
            return value

        return ops(len(word1)-1, len(word2)-1)
        # return 0
        