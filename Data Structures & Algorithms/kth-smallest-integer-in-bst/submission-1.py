# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        def dfs(root, count):
            left_count, right_count, done, value = 0, 0, False, -1
            if root.left:
                (left_count, done, value) = dfs(root.left, count)
            if done:
                return (left_count+1, True, value)
            print(f"hello {root.val}, {count+left_count+1}")
            if count+left_count+1 == k:
                ans = root.val
                return k,True,root.val
            if root.right:
                (right_count,done, value) = dfs(root.right, count+left_count+1)
            print(root.val, value)
            return left_count+right_count+1, done, value
        total, found, ans = dfs(root,0)
        return ans
            
        