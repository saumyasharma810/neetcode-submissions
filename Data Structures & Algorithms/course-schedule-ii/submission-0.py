class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph =  [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            indegree[prereq[0]]+=1
        next_nodes = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                next_nodes.append(i)
        visited = []
        while next_nodes:
            for node in graph[next_nodes[0]]:
                indegree[node]-=1
                if indegree[node] == 0:
                    next_nodes.append(node)
            visited.append(next_nodes[0])
            next_nodes.popleft()
        return visited if len(visited) == numCourses else []