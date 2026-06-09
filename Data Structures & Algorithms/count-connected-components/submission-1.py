class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(i, visited):
            visited.add(i)
            for neighbor in graph[i]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i,visited)
                components+=1
        return components

        