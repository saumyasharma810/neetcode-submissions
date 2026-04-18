class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_pq = []
        l,r = 0,k-1
        for i in range(k-1):
            heapq.heappush(max_pq, (-nums[i],i))
        while r<len(nums):
            heapq.heappush(max_pq, (-nums[r],r))
            while max_pq[0][1] < l:
                heapq.heappop(max_pq)
            result.append(-max_pq[0][0])
            l+=1
            r+=1
        return result
            


        
        