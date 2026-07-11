class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a,b = None,None
        freq_a, freq_b = 0,0
        for i in range(len(nums)):
            if a==nums[i]:
                freq_a += 1
                continue
            if b == nums[i]:
                freq_b += 1
                continue
            if a==None:
                a = nums[i]
                freq_a = 1
                continue
            if b==None:
                b = nums[i]
                freq_b = 1
                continue
            freq_a -= 1
            freq_b -= 1
            if freq_a == 0:
                a = None
            if freq_b == 0:
                b = None
        freq_a, freq_b = 0,0
        for i in range(len(nums)):
            if nums[i] == a:
                freq_a+=1
            elif nums[i] == b:
                freq_b += 1
        lst = []
        if freq_a > len(nums)//3:
            lst.append(a)
        if freq_b > len(nums)//3:
            lst.append(b)
        return lst
        