class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        loops = math.gcd(n,k)
        for i in range(loops):
            temp = nums[i] # 1
            x = (i+k)%n # 4
            while x!=i: # 4 != 0
                temp2 = nums[x] # 5
                nums[x] = temp # 1
                temp = temp2 # 5
                x=(x+k)%n # 0
            nums[x] = temp 
        
    # 12345678
    # 





        