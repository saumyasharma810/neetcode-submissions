class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        can_reach = {}


        def reach(i):
            if i == 0:
                return True
            if i in can_reach:
                return can_reach[i]
            for k in range(0,i):
                if nums[k]+k >= i and reach(k):
                    can_reach[i] = True
                    return True
            can_reach[i] = False
            return False
        
        return reach(n-1)

        