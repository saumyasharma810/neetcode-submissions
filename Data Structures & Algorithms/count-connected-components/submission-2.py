class Solution:
    class dsu:
        def __init__(self,n):
            self.parent = [i for i in range(n)]
        
        def union(self,a,b):
            x,y = self.get_parent(a), self.get_parent(b)
            if x == y:
                return False
            if y > x:
                x,y = y,x
            self.parent[y] = x
            return True
        
        def get_parent(self,a):
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
            
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = self.dsu(n)
        comp = n
        for edge in edges:
            if d.union(edge[0], edge[1]):
                comp -=1
        return comp
        

        