class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        pq = []
        for i in range(k):
            pq.append(nums[i])
        heapq.heapify(pq)
        for i in range(k,len(nums)):
            if nums[i] > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq,nums[i])
        return pq[0]

        