class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(0, amount+1):
                if coins[i]+j <= amount:
                    dp[coins[i]+j] += dp[j]
        return dp[amount]
        


            
            

        