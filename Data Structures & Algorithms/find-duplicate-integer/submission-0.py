class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while True:
            if nums[i] == -1:
                return i
            j = nums[i]
            nums[i] = -1
            i = j
        return -1
        