# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_value):
            if not node:
                return
            nonlocal count
            if node.val >= max_value:
                count += 1
            dfs(node.left, max(max_value, node.val))
            dfs(node.right, max(max_value, node.val))
        dfs(root, root.val)
        return count
        