class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}

        def combinations(i, total):
            if i >= len(coins):
                return 0
            if total > amount:
                return 0
            if total == amount:
                return 1
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = combinations(i, total+coins[i]) + combinations(i+1, total)
            return dp[(i,total)]
        
        return combinations(0, 0)
        


            
            

        