class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        sums = float("-inf")
        for num in nums:
            if sums < 0:
                sums = num
            else:
                sums += num
            maxi = max(maxi,sums)
        return maxi
        