class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 12 -> 1, 5, 10
        # 11, 7, 2
        # 10, 6, 1, 6, 2, 1 -> 10,6,2,1
        # 9, 5, 0, 5, 1, 0, 5, 1, 1, 0

        dp = [-2] * (amount+1)

    
        def coins_needed(n):
            if n < 0:
                return -1
            if n == 0:
                return 0
            if dp[n] != -2:
                return dp[n]
            min_coins = float("inf")
            for coin in coins:
                coins_need = coins_needed(n-coin)
                if coins_need == -1:
                    continue
                min_coins = min(min_coins, coins_needed(n-coin)+1)
            if min_coins == float("inf"):
                dp[n] = -1
                return -1
            dp[n] = min_coins
            return min_coins

        return coins_needed(amount)
