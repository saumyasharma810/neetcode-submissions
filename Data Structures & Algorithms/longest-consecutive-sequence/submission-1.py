class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = defaultdict(int)
        max_length = 0
        for num in nums:
            k = num
            if k in length:
                continue

            if k-1 in length:
                length[k] = length[k-1]+1
            else:
                length[k] = 1

            while k+1 in length:
                length[k+1] = length[k]+1
                k+=1
            
            max_length = max(max_length, length[k])
            
        return max_length