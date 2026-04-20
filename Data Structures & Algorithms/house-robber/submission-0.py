class Solution:
    def rob(self, nums: List[int]) -> int:
        max_amount = [-1] * len(nums)
        max_amount[0] = nums[0]
        if len(nums) == 1:
            return max_amount[0]
        max_amount[1] = max(max_amount[0],nums[1])
        for i in range(2,len(nums)):
            max_amount[i] = max(max_amount[i-1],max_amount[i-2]+nums[i])
        return max_amount[len(nums)-1]
        