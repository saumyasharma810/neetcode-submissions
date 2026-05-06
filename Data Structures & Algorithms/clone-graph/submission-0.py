"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        def dfs(node_og):
            if node_og in visited:
                return
            new_node = Node(node_og.val)
            visited[node_og] = new_node
            for neighbor in node_og.neighbors:
                dfs(neighbor)
                new_node.neighbors.append(visited[neighbor])  
        dfs(node)
        return visited[node]
                







        