class Solution:
    class dsu:
        def __init__(self, n):
            self.parent = [i for i in range(n)]
        
        def union(self,a,b):
            pa, pb = self.find(a), self.find(b)
            if pa == pb:
                return False
            pa, pb = min(pa,pb), max(pa,pb)
            self.parent[pb] = pa
            return True
            
    
        def find(self,a):
            temp = a
            while temp != self.parent[temp]:
                temp = self.parent[temp]
            root = temp
            temp = a
            while temp != root:
                temp2 = self.parent[temp]
                self.parent[temp] = root
                temp = temp2
            return root

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        # no cycle
        d = self.dsu(n)
        for edge in edges:
            if not d.union(edge[0], edge[1]):
                return False
        return True
        