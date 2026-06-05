class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a,b,ans = 1,-11,-11
        i = 0
        neg = False
        while i < len(nums):
            if nums[i] == 0:
                ans = max(ans,0)
                i+=1
                continue
            while i < len(nums) and nums[i]!=0:
                a *= nums[i]

                if neg:
                    b*=nums[i]

                ans = max(ans,a,b)
                
                if nums[i] < 0 and not neg:
                    neg = True
                    b = 1
                
                print(i,ans)
                
                i+=1
            a = 1
            b = -11
            neg = False
        return ans
            
            
            
        