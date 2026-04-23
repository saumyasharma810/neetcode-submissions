# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def same(self, a, b):
        if not a and not b:
            return True
        if not a:
            return False
        if not b:
            return False
        if a.val == b.val and self.same(a.left,b.left) and self.same(a.right,b.right):
            return True
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            return self.same(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        return False
        
        
        
        