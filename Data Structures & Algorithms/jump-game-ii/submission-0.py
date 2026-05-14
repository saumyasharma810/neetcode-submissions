class Solution:
    def jump(self, nums: List[int]) -> int:
        min_step = [float("inf")] * len(nums)
        min_step[0] = 0
        for i in range(len(nums)):
            if min_step[i] == float("inf"):
                continue
            end = min(i+nums[i]+1, len(nums))
            for j in range(i,end):
                min_step[j] = min(min_step[j], min_step[i]+1)
        return min_step[len(nums)-1]