# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = None
        def dfs(node):
            nonlocal ancestor
            if not node:
                return False
            if node.val == p.val or node.val == q.val:
                if dfs(node.left) or dfs(node.right):
                    ancestor = node
                return True
            if dfs(node.left) and dfs(node.right):
                ancestor = node
                return True
            if dfs(node.left) or dfs(node.right):
                return True
            return False
        dfs(root)
        return ancestor