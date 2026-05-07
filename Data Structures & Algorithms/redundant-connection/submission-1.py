class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        for edge in edges:
            p1, p2 = parent[edge[0]], parent[edge[1]]

            temp1 = p1
            while parent[temp1] != temp1:
                temp1 = parent[temp1]
            temp2 = p2
            while parent[temp2] != temp2:
                temp2 = parent[temp2]
            
            if temp1 == temp2:
                return edge

            # make all parent as the minimum of temp1 and temp2
            p = min(temp1, temp2)

            while parent[p1]!=p:
                p1_temp = parent[p1]
                parent[p1] = p
                p1 = p1_temp

            while parent[p2]!=p:
                p2_temp = parent[p2]
                parent[p2] = p
                p2 = p2_temp

        return []









        