class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)
        while len(max_heap) > 1:
            a = heapq.heappop_max(max_heap)
            b = heapq.heappop_max(max_heap)
            if a == b:
                continue
            heapq.heappush_max(max_heap, a-b)
        if not max_heap:
            return 0
        return max_heap[0]

        