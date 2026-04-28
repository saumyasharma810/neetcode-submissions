class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max_heap for freq
        # queue for when to add in max_heap
        freq = [0]*26
        for task in tasks:
            freq[ord(task)-ord('A')] += 1
        freq.sort(reverse=True)
        max_heap = []
        queue = deque()
        for i in range(26):
            if freq[i] == 0:
                break
            heapq.heappush_max(max_heap, freq[i])
        time = 0
        while max_heap or queue:
            time+=1
            if max_heap:
                t = heapq.heappop_max(max_heap)
                if t-1 != 0:
                    queue.append((time+n,t-1))
            while queue and queue[0][0] <= time:
                heapq.heappush_max(max_heap, queue.popleft()[1])
            
        return time

        
        



        