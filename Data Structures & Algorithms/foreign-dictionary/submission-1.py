class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        n = len(words)
        queue = deque()
        char_list = set()

        for i in range(n):
            for j in range(len(words[i])):
                char_list.add(words[i][j])

        for i in range(n):
            for j in range(i+1,n):
                min_len = min(len(words[i]), len(words[j]))
                equal = True
                for k in range(min_len):
                    if words[i][k] != words[j][k]:
                        graph[words[i][k]].add(words[j][k])
                        equal = False
                        break
                    if equal and len(words[i]) > len(words[j]):
                        return ""
                
        
        for a,set_b in graph.items():
            if a not in indegree:
                indegree[a] = 0
            for x in set_b:
                indegree[x] += 1


        for char in char_list:
            if char not in indegree:
                indegree[char] = 0
            if indegree[char] == 0:
                queue.append(char)

        print(graph)
        print(indegree)

        # topo sort
        sorted_alpha = ''
        while queue:
            char = queue.popleft()
            sorted_alpha += char
            for neighbor in graph[char]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        print(sorted_alpha)

                
        
        return sorted_alpha if len(sorted_alpha) == len(char_list) else ""






        



        
        