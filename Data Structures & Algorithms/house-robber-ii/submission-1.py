class Solution:
    def rob(self, nums: List[int]) -> int:
        # from 0 till n-2
        max_value = [0] * (len(nums))
        max_value[0] = nums[0]
        for i in range(1,len(nums)-1):
            if i == 1:
                max_value[i] = max(max_value[i-1], nums[i])
            else:
                max_value[i] = max(max_value[i-1], nums[i]+max_value[i-2])
        max_rob = max_value[len(nums)-2]
        print(max_rob)
        max_value = [0] * (len(nums))
        # from 1 till n-1
        for i in range(1,len(nums)):
            if i == 1:
                max_value[i] = nums[i]
            elif i == 2:
                max_value[i] = max(max_value[i-1], nums[i])
            else:
                max_value[i] = max(max_value[i-1], nums[i]+max_value[i-2])
        
        return max(max_rob, max_value[len(nums)-1])
        