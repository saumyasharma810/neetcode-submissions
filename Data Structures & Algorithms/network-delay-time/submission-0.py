class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        pq = [(0,k)] # time, node
        heapq.heapify(pq)
        visited = set()
        
        graph = defaultdict(list)
        for lst in times:
            graph[lst[0]].append((lst[1], lst[2])) # neighbor, add_time

        total_time = 0
        while pq:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue   
            # print(time,node)
            total_time = max(time,total_time)
            visited.add(node)
            for neighbor, add_time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (time+add_time, neighbor))
        print(len(visited))
        if len(visited) != n:
            return -1
        return total_time

                



        