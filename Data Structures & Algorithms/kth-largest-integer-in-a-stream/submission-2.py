class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.need = k
        heapq.heapify(self.heap)
        for i in range(len(nums)-k):
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.need:
            heapq.heappop(self.heap)
        return self.heap[0]
        
