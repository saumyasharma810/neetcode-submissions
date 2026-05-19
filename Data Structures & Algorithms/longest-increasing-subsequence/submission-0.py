class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = [1] * len(nums)
        max_length = 0
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    length[i] = max(length[i], length[j]+1)
            max_length = max(max_length, length[i])
        return max_length


        