class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[-1 for _ in range(len(text1))] for _ in range(len(text2))]

        def lcs(t1_ind, t2_ind):
            if t1_ind < 0 or t2_ind < 0:
                return 0
            if dp[t2_ind][t1_ind] != -1:
                return dp[t2_ind][t1_ind]
            maxi_lcs = max(lcs(t1_ind-1,t2_ind), lcs(t1_ind,t2_ind-1))
            if text1[t1_ind] == text2[t2_ind]:
                maxi_lcs = max(maxi_lcs, 1 + lcs(t1_ind-1,t2_ind-1))
            dp[t2_ind][t1_ind] = maxi_lcs
            return maxi_lcs
        
        max_lcs = lcs(len(text1)-1,len(text2)-1)
        
        return max_lcs

            
        