# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def same(a,b):
            if not a and not b:
                return True
            if not a:
                return False
            if not b:
                return False
            if a.val == b.val and same(a.left,b.left) and same(a.right,b.right):
                return True
            return False
        
        return same(p,q)

        