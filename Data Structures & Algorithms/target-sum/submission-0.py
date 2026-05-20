class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def combis(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = combis(i+1, total+nums[i]) + combis(i+1, total-nums[i])
            return dp[(i,total)]
        
        return combis(0,0)
        