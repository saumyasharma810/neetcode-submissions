class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if len(word1) == 0 and len(word2)==0:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2)==0:
            return len(word1)

        dp = [[len(word1)+len(word2)] * len(word2) for _ in range(len(word1))]

        for i in range(len(word1)):
            for j in range(len(word2)):
                if i == 0 and j == 0: 
                    dp[i][j] = 0 if word1[i]==word2[j] else 1
                elif i == 0:
                    dp[i][j] = min(j, dp[i][j-1]+1) if word1[i]==word2[j] else min(j+1, dp[i][j-1]+1)
                elif j == 0:
                    dp[i][j] = min(i, dp[i-1][j]+1) if word1[i]==word2[j] else min(i+1, dp[i-1][j]+1)
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)
                    if word1[i]==word2[j]:
                        dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                        
        return dp[len(word1)-1][len(word2)-1]
        