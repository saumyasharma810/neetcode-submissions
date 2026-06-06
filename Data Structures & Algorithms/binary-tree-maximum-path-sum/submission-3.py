# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _total_value(self, root, dp):
        if not root:
            return 0
        if root in dp:
            return dp[root]
        dp[root] = max(self._total_value(root.left, dp), self._total_value(root.right, dp))+root.val
        # print(root.val, dp)
        return dp[root] if dp[root] > 0 else 0


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def maxSum(rootNode):
            if not rootNode:
                return float("-inf")
            value = rootNode.val + max(0,self._total_value(rootNode.left, dp)) + max(0,self._total_value(rootNode.right, dp))
            print(rootNode.val)
            # print("value",value)
            return max(maxSum(rootNode.left), maxSum(rootNode.right), value)
        return maxSum(root)
        