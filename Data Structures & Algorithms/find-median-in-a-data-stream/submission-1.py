class MedianFinder:

    def __init__(self):
        self.max_heap = [] # smaller values always more or equal
        self.min_heap = [] # larger values
        

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush_max(self.max_heap, num)
            return
        if num >= self.max_heap[0]:
            if len(self.min_heap) == len(self.max_heap):
                heapq.heappush(self.min_heap, num)
                heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if len(self.min_heap) == len(self.max_heap):
                heapq.heappush_max(self.max_heap, num)
            else:
                heapq.heappush_max(self.max_heap, num)
                heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))
        
        

    def findMedian(self) -> float:
        if self.min_heap and len(self.min_heap) == len(self.max_heap):
            return ((self.min_heap[0] + self.max_heap[0]) / 2)
        return self.max_heap[0]

        
        