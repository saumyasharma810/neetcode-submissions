class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if i!=j:
                    graph[i].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), j))
                    graph[j].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), i))
        curr = 0
        pq = graph[curr]
        heapq.heapify(pq)
        mst = 1
        score = 0
        visited = [False] * len(points)
        visited[0] = True
        while pq and mst != len(points):
            while pq and visited[pq[0][1]]:
                heapq.heappop(pq)
            if pq:
                curr = pq[0][1]
                mst+=1
                score+=pq[0][0]
                visited[curr] = True
            for point in graph[curr]:
                heapq.heappush(pq,point)
        return score

        