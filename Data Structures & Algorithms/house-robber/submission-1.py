class Solution:
    def rob(self, nums: List[int]) -> int:
        max_amount = [-1] * len(nums)
        def amount(n):
            if n < 0:
                return 0
            if max_amount[n] != -1:
                return max_amount[n]
            max_amount[n] = max(amount(n-1), amount(n-2)+nums[n])
            return max_amount[n]
        return amount(len(nums)-1)
        