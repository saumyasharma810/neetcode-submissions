class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = [False] * n
        reach[0] = True
        for i in range(n):
            if reach[i]:
                for j in range(i,i+nums[i]+1):
                    if j < n:
                        reach[j] = True
        return reach[n-1]

        