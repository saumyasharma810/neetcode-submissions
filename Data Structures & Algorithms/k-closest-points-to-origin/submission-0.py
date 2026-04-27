class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            min_heap.append(((((point[0])**2+(point[1])**2) ** 0.5),point))
        heapq.heapify(min_heap)
        lst = []
        for _ in range(k):
            lst.append(min_heap[0][1])
            heapq.heappop(min_heap)
        return lst
        

        