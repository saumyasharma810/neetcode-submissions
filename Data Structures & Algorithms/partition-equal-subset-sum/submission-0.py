class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        partitions = {}
        def dfs(i, summ):
            if i == len(nums):
                if summ == total//2:
                    return True
                return False
            if (i,summ) in partitions:
                return partitions[(i,summ)]
            if dfs(i+1, summ) or dfs(i+1, summ+nums[i]):
                partitions[(i,summ)] = True
                return True
            partitions[(i,summ)] = False
            return False
            
        if dfs(0,0):
            return True
        return False
        