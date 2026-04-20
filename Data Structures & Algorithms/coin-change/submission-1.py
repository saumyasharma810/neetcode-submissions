class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 12 -> 1, 5, 10
        # 11, 7, 2
        # 10, 6, 1, 6, 2, 1 -> 10,6,2,1
        # 9, 5, 0, 5, 1, 0, 5, 1, 1, 0

        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i + coin > amount:
                    continue
                dp[i+coin] = min(dp[i+coin], dp[i]+1)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
