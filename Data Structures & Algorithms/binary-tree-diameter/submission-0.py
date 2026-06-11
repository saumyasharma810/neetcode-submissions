# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:



    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def max_len(root):
            if not root:
                return 0
            return max(max_len(root.left), max_len(root.right))+1
        
        value = max_len(root.left) + max_len(root.right)

        return max(value, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    


        