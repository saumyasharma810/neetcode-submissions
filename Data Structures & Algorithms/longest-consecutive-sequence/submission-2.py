class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = set()
        max_length = 0
        for num in nums:
            length.add(num)
        
        for num in nums:
            if not num-1 in length:
                k = num
                while k in length:
                    k+=1
                max_length = max(k-num, max_length)
            
        return max_length