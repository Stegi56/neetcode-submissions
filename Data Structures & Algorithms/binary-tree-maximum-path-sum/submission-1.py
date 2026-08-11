# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(n: Optional[TreeNode]) -> int:
            nonlocal res
            if n:
                l = dfs(n.left)
                r = dfs(n.right)
                bestPath = max(
                    n.val,
                    n.val + l,
                    n.val + r
                )
                bestChainRoot = max(
                    bestPath,
                    n.val + l + r
                )
                res = max(res, bestChainRoot, bestPath)
                return bestPath

            return 0

        dfs(root)
        return res