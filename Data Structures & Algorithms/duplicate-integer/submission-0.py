class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevHash = {}

        for n in nums:
            if n in prevHash:
                return True
            else:
                prevHash[n] = True

        return False
        